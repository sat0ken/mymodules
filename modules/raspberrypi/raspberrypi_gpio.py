#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
'supported_by': 'community'}

import RPi.GPIO as GPIO
import time

def do_gpio(pin_setup, gpio_pin, led_cnt):

    GPIO.setmode(GPIO.BCM)

    if pin_setup == 'OUT':
        GPIO.setup(gpio_pin, GPIO.OUT)
    else:
        GPIO.setup(gpio_pin, GPIO.IN)

    for i in range(led_cnt):
        GPIO.output(gpio_pin, True)
        time.sleep(1)
        GPIO.output(gpio_pin, False)
        time.sleep(1)

    GPIO.cleanup()

def main():

    module = AnsibleModule(
        argument_spec=dict(
            setup=dict(type='str', required=True),
            pin=dict(type='int', required=True),
            count=dict(type='int', required=True)
        )
    )

    pin_setup = module.params['setup']
    gpio_pin = module.params['pin']
    led_cnt = module.params['count']

    do_gpio(pin_setup, gpio_pin, led_cnt)

    module.exit_json(msg='GPIO action successfully')

if __name__ == '__main__':
    main()
