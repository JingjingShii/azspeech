# -*- coding: utf-8 -*-
#
# Time-stamp: <Saturday 2020-06-27 06:47:14 AEST Graham Williams>
#
# Copyright (c) Togaware Pty Ltd. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# ml transcribe azspeech <path>

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import os
import sys
import time
import argparse

import azure.cognitiveservices.speech as speechsdk

from mlhub.pkg import azkey
from mlhub.utils import get_cmd_cwd

#-----------------------------------------------------------------------
# Process the command line
#-----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path to audio file')

args = option_parser.parse_args()

path = os.path.join(get_cmd_cwd(), args.path)

#----------------------------------------------------------------------
# Request subscription key and location from user.
#----------------------------------------------------------------------

SERVICE   = "Speech"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

key, location = azkey(KEY_FILE, SERVICE, connect="location", verbose=False)

#-----------------------------------------------------------------------
# Trasnscribe some spoken words from a file.
#-----------------------------------------------------------------------

# Create a callback to terminate the transcription once the full audio
# has been transcribed.

done = False

def stop_cb(evt):
    """Callback to stop continuous recognition upon receiving an event `evt`"""
    speech_recognizer.stop_continuous_recognition()
    global done
    done = True

# Create an instance of a speech config with the provided subscription
# key and service region. Then create an audio configuration to load
# the audio from file rather than from microphone. A sample audio file
# is available as harvard.wav from:
#
# https://github.com/realpython/python-speech-recognition/raw/master/
# audio_files/harvard.wav
#
# A recognizer is then created with the given settings.

speech_config = speechsdk.SpeechConfig(subscription=key, region=location)
audio_config  = speechsdk.audio.AudioConfig(use_default_microphone=False, filename=path)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                               audio_config=audio_config)

# We connect callbacks to the events fired by the speech
# recognizer. Most are commented out as examples here to allow tracing
# if you are interested in exploring the interactions with the server.
#
# speech_recognizer.recognizing.connect(lambda evt:
#                                       print('RECOGNIZING: {}'.format(evt)))
# speech_recognizer.session_started.connect(lambda evt:
#                                           print('STARTED: {}'.format(evt)))
# speech_recognizer.session_stopped.connect(lambda evt:
#                                           print('STOPPED {}'.format(evt)))
# speech_recognizer.canceled.connect(lambda evt:
#                                    print('CANCELED {}'.format(evt)))

# This callback provides the actual transcription.

speech_recognizer.recognized.connect(lambda evt:
                                     print('{}'.format(evt.result.text)))

# Stop continuous recognition on either session stopped or canceled
# events.

speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

# Start continuous speech recognition, and then perform
# recognition. For long-running recognition we use
# start_continuous_recognition().

speech_recognizer.start_continuous_recognition()
while not done: time.sleep(.5)

