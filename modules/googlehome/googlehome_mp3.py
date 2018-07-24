#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'community'}

import pychromecast
import time

def main():

    ansible_facts = dict()
    module = AnsibleModule(
        argument_spec=dict(
            device_name=dict(type='str', required=True),
            mp3=dict(type='str', required=True)
        )
    )
    device = module.params['device_name']
    mp3_url = module.params['mp3']
    casts = pychromecast.get_chromecasts()
    cast = next(cc for cc in casts if cc.device.friendly_name == device)
    time.sleep(1)
    if not cast.is_idle:
        cast.quit_app()
        time.sleep(5)

    cast.play_media((mp3_url), "video/mp3")
    time.sleep(2)
    module.exit_json(msg="OK", changed=False)

if __name__ == '__main__':
    main()
