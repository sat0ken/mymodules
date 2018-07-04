#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'community'}

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.network.dna import dna
import json

api_url     = '/api/v1/topology'

def get_networks(module, dna_url, token):

    headers={
        'X-Auth-Token': '{}'.format(token),
        'Content-type': 'application/json',
    }
    response, info = fetch_url(module=module, url=dna_url, headers=headers, method='GET') 

    if info['status'] != 200:
        module.fail_json(rc=1, msg="HTTP Status Erro %s" % dna_url)

    if response is not None:
        data = json.loads(response.read())

    return data


def main():
    network_device = dict()

    module = AnsibleModule(
        argument_spec=dict(
            dna_url=dict(type='str', required=True, no_log=True),
            dna_username=dict(type='str', required=True, no_log=True),
            dna_password=dict(type='str', required=True, no_log=True),
            validate_certs=dict(type='bool', default=False),
            api_endpoint=dict(type='str', required=True, no_log=True)
        )
    )

    dna_url  = module.params['dna_url']
    dna_username = module.params['dna_username']
    dna_password = module.params['dna_password']
    api_endpoint = module.params['api_endpoint']

    token = dna.get_token(dna_username, dna_password)

    request_url = dna_url + api_url + api_endpoint
    network_device = get_networks(module, request_url, token)

    module.exit_json(changed=False, networkdevice_facts=network_device)

if __name__ == '__main__':
    main()
