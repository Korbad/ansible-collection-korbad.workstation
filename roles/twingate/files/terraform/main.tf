resource "twingate_remote_network" "korbad_network" {
  name = "JoshOffice"
  location = "ON_PREMISE"
}

resource "twingate_resource" "korbad_resource" {
  name = "John's HQ"
  address = "192.168.1.10"
  remote_network_id = var.remote_network

  protocols {
    allow_icmp = false
    tcp  {
      policy = "RESTRICTED"
      ports = var.allowed_ports
    }
    udp {
      policy = "DENY_ALL"
    }
  }
  
  access {
    group_ids = [
      "R3JvdXA6ODc0NTU="
    ]
  }
}