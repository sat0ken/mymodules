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


def create_mp3(mp3_file, mesg):
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.types.SynthesisInput(text=mesg)
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='ja_JP',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    with open(mp3_file, 'wb') as out:
        out.write(response.audio_content)

def main():

    ansible_facts = dict()
    module = AnsibleModule(
        argument_spec=dict(
            device_name=dict(type='str', required=True),
            mp3_server=dict(type='str', required=True),
            mp3_folder=dict(type='str', required=True),
            mp3_file=dict(type='str', required=True),
            texttospeech=dict(type='str', required=True)
        )
    )


    device = module.params['device_name']
    mp3_server = module.params['mp3_server']
    mp3_folder = module.params['mp3_folder']
    mp3_file = module.params['mp3_file']
    texttospeech = module.params['texttospeech']

    file_path = mp3_folder + "/" + mp3_file
    create_mp3(file_path, texttospeech)

    casts = pychromecast.get_chromecasts()
    cast = next(cc for cc in casts if cc.device.friendly_name == device)
    time.sleep(1)
    if not cast.is_idle:
        cast.quit_app()
        time.sleep(5)

    mp3_path = mp3_server + "/" + mp3_file
    cast.play_media((mp3_path), "video/mp3")
    time.sleep(2)
    module.exit_json(msg="OK", changed=False)

if __name__ == '__main__':
    main()
