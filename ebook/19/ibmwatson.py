from __future__ import unicode_literals
import requests
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import codecs
import sys  
import os

def getFolderName():
	dir_name= (os.getcwd())
	folders=dir_name.split('/')
	length=len(folders)
	return folders,length

def main():	
	folders,length = getFolderName()
	reload(sys)  
	os.system('python sentsplit.py')
	l=open("length.txt")
	le=l.read()
	c=[0]*int(le)
	b=[0]*int(le)   
	d=[0]*int(le)
	sys.setdefaultencoding('utf8')
	url = 'https://stream.watsonplatform.net/text-to-speech/api'
	username='269a7a7e-f263-4642-a93d-ae1c53a96a37',
	password='FGmXDjefTnZd'
	text = 'hello Australia'
	voice = 'en-GB_KateVoice'
	accept = ''

	for i in range(int(le)):
		c[i]=open("b%d.txt" %i)
		b[i]=c[i].read()
		#d[i]=c[i].read(1)
		#os.system('file b%d > ')
		#print not d[i]
		if os.stat("b%d.txt" %i).st_size == 0:
			#print "hello %r" %b[i]
			continue
		
		else:
			say_this = b[i]
			print "a file is created"
			text_to_speech = TextToSpeechV1(username='269a7a7e-f263-4642-a93d-ae1c53a96a37',password='FGmXDjefTnZd')          
			y = len("en-US_AllisonVoice")
			fn = 'output_'+"%sen-US_AllisonVoice%d" %(folders[length-1],i) +'.wav'
			with open(join(dirname(__file__),"/home/arvind/Desktop/project/tesseract_testing/ebook/audio/"+fn), 'wb') as audio_file:
				audio_file.write(text_to_speech.synthesize(say_this,voice="en-US_AllisonVoice"))
		c[i].close()

main()

