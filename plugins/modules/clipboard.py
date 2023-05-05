#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import pyperclip

def main():
    module = AnsibleModule(
        argument_spec=dict(
            content=dict(type='str', required=True),
        ),
        supports_check_mode=True
    )

    content = module.params['content']

    if module.check_mode:
        module.exit_json(changed=True)

    try:
        pyperclip.copy(content)
        module.exit_json(changed=True, content=content)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()
