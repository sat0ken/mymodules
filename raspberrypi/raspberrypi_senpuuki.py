#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'community'}

def main():

    module = AnsibleModule(
        argument_spec=dict(
            power_state=dict(type='str', required=True),
        )
    )

    power = module.params['power_state']
    rtn = ""

    if power == "ON":
        cmd = "irsend SEND_ONCE senpuuki on"
    else:
        cmd = "irsend SEND_ONCE senpuuki off"

    (rc, out, err) = module.run_command(cmd)
    if rc == 0:
        module.exit_json(msg="OK", changed=True)

if __name__ == '__main__':
    main()
