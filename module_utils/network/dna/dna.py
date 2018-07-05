#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'community'}

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url

import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()
import json

login_url   = 'https://sandboxdnac.cisco.com/api/system/v1/identitymgmt/token'

def get_token(u_name, u_pass):

    headers={
        'Content-type': 'application/json',
    }

    response = requests.post(url=login_url, headers=headers, auth=HTTPBasicAuth(u_name, u_pass), verify=False)
    return response.json()["Token"]

