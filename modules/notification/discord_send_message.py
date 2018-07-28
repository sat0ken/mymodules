#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'community'}

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
import discord
import asyncio
import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url

def send_message(module, token, channel_id, msg):

    baseURL = "https://discordapp.com/api/channels/{}/messages".format(channel_id)
    headers = { "Authorization":"Bot {}".format(token),
                "User-Agent":"myBotThing (http://some.url, v0.1)",
                "Content-Type":"application/json", }
    json_data = json.dumps ({"content": msg })

    response, info = fetch_url(module=module, url=baseURL, headers=headers, method='POST', data=json_data)

    if info['status'] != 200:
        module.fail_json(rc=1, msg="failed to send messages")



def main():
    module = AnsibleModule(
        argument_spec=dict(
            token=dict(type='str', required=True, no_log=True),
            channel_id=dict(type='str', required=True, no_log=True),
            msg=dict(type='str', required=True)
        )
    )

    token = module.params['token']
    channel_id = module.params['channel_id']
    msg = module.params['msg']

    send_message(module, token, channel_id, msg)

    module.exit_json(msg="OK")

if __name__ == '__main__':
    main()
