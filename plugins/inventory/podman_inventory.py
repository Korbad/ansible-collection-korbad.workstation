#!/usr/bin/env python

from ansible.plugins.inventory import BaseInventoryPlugin
import json
import subprocess
import podman

class InventoryModule(BaseInventoryPlugin):

    NAME = 'ansible_collections.korbad.workstation.plugins.inventory.podman_inventory'

    def verify_file(self, path):
        return super(InventoryModule, self).verify_file(path) and path.endswith('podman_inventory.yml')

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)

        # Call Podman functions
        podman_data = self.get_podman_containers()
        pod_data = self.get_podman_pods()

        # Generate inventory
        self.inventory = self.generate_inventory(podman_data, pod_data)
        self.populate_inventory()

    def get_podman_containers(self):
        with podman.Client() as client:
            container_data = [(container.id, container.name, container.pod) for container in client.containers.list()]
            print("Container data:", container_data)  # Debug print
            return container_data

    def get_podman_pods(self):
        with podman.Client() as client:
            pod_data = [(pod.id, pod.name) for pod in client.pods.list()]
            print("Pod data:", pod_data)  # Debug print
            return pod_data

    def generate_inventory(self, podman_data, pod_data):
        inventory = {
            '_meta': {
                'hostvars': {}
            },
            'all': {
                'children': ['ungrouped', 'pods']
            },
            'pods': {
                'children': []
            },
            'ungrouped': {
                'hosts': []
            }
        }

        for pod_id, pod_name in pod_data:
            inventory['pods']['children'].append(pod_name)
            inventory[pod_name] = {
                'hosts': []
            }

        for container_id, container_name, container_pod_id in podman_data:
            if container_pod_id == "":
                inventory['ungrouped']['hosts'].append(container_name)
            else:
                for pod_id, pod_name in pod_data:
                    if container_pod_id == pod_id:
                        inventory[pod_name]['hosts'].append(container_name)
                        break

        return inventory

    def populate_inventory(self):
        for group_name, group_data in self.inventory.items():
            if group_name == '_meta':
                continue
            self.inventory.add_group(group_name)
            for host in group_data.get('hosts', []):
                self.inventory.add_host(host, group_name)
            for child in group_data.get('children', []):
                self.inventory.add_group(child)
                self.inventory.add_child(group_name, child)
