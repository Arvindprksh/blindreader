from __future__ import unicode_literals
import requests
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import codecs
import sys  
import os
reload(sys)  
file1 = open("t2sforprompt.txt")
word = file1.read()
sys.setdefaultencoding('utf8')
url = 'https://stream.watsonplatform.net/text-to-speech/api'
username='269a7a7e-f263-4642-a93d-ae1c53a96a37',
password='FGmXDjefTnZd'
text = 'hello Australia'
voice = 'en-GB_KateVoice'
accept = ''
say_this = word
text_to_speech = TextToSpeechV1(username='269a7a7e-f263-4642-a93d-ae1c53a96a37',password='FGmXDjefTnZd')
y = len("en-US_AllisonVoice")
i = 0
#for i in range (y):
fn = 'output_'+"en-US_AllisonVoiceforprompt"+'.wav'
with open(join(dirname(__file__),"/home/arvind/Desktop/project/v2/ebook/"+fn), 'wb') as audio_file:
	audio_file.write(text_to_speech.synthesize(say_this,voice="en-US_AllisonVoice"))
