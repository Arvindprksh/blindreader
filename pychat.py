#!/usr/bin/env python
import os
import time
import math
import random
flag = 0
def rewindfunc():
	re=open("rewindflag.txt","r+")
	os.system(">rewindflag.txt")
	re.write("1")
	re.close()
	os.system('python play.py')
	re=open("rewindflag.txt","r+")
	os.system(">rewindflag.txt")
	re.write("0")
	re.close()
def rand():
	r=(int)(math.ceil(random.random()*100))
	if(r>0 and r<30):
		return 1
	elif(r>=30 and r<60):
		return 2
	elif(r>=60 and r<=100):
		return 3

def googleread():
        os.system('python googlestt.py')
	src=open("s2t.txt")
	inp1= src.read()
	return inp1

def readitaloud(string):
	dest = open("t2s.txt",'r+')
	os.system(">t2s.txt")
	dest.write(string)
	dest.close()
	os.system('python ibmwatsonforace.py')
	os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav')
def readitaloudforprompt(string):
	dest = open("t2sforprompt.txt",'r+')
	os.system(">t2sforprompt.txt")
	dest.write(string)
	dest.close()
	os.system('python ibmwatsonforprompt.py')
	os.system('vlc --no-one-instance --play-and-exit output_en-US_AllisonVoiceforprompt.wav')

def chat(inp):
	if((inp.find("start",0,len(inp))!=-1) and (inp.find("reading",0,len(inp))!=-1)):
		flag=1
		re=open("rewindflag.txt","r+")
		os.system(">rewindflag.txt")
		re.write("0")
		if(rand()==1):
			os.system('vlc  --no-one-instance --play-and-exit start1.wav ')
		elif(rand()==2):
			os.system('vlc  --no-one-instance --play-and-exit start2.wav ')
		elif(rand()==3):
			os.system('vlc  --no-one-instance --play-and-exit start3.wav ')

		os.system("./blindread1.sh &")
		return 1
	
	elif((inp.find("pause",0,len(inp))!=-1) or (inp.find("hold",0,len(inp))!=-1)):
		#readitaloud("Ok... lets pause right here.. we will be back whenever you want")
		os.system('pkill -STOP vlc')
		return 1
	elif((inp.find("continue",0,len(inp))!=-1) or (inp.find("resume",0,len(inp))!=-1)):
		#readitaloud("Right.. Shall we begin now..")
		os.system('pkill -CONT vlc')
		rewindfunc()
		return 1

	elif((inp.find("replay",0,len(inp))!=-1) or (inp.find("back",0,len(inp))!=-1)):
		#readitaloud("Right.. Shall we begin now..")
		re=open("rewindflag.txt","r+")
		os.system(">rewindflag.txt")
		re.write("1")
		re.close()
		os.system('python play.py')
		re=open("rewindflag.txt","r+")
		os.system(">rewindflag.txt")
		re.write("0")
		re.close()
		return 1
	
	elif((inp.find("stop",0,len(inp))!=-1) and (inp.find("book",0,len(inp))!=-1)):
		os.system('pkill -9 vlc')
		if(rand()==1):
			os.system('vlc  --no-one-instance --play-and-exit stop1.wav ')
		elif(rand()==2):
			os.system('vlc  --no-one-instance --play-and-exit stop2.wav ')
		elif(rand()==3):
			os.system('vlc  --no-one-instance --play-and-exit stop3.wav ')
		dictate=0
		return 1


	elif((inp.find("define",0,len(inp))!=-1) or (inp.find("definition",0,len(inp))!=-1)):
		print "ok"
		dest = open("txt1.txt",'r+')
		os.system(">txt1.txt")
		dest.write(inp)
		dest.close()
		os.system('pkill -STOP vlc')
		os.system('python pydictionary1.py')
		os.system('python ibmwatsonfordict.py')
		os.system('vlc --no-one-instance --play-and-exit output_en-US_AllisonVoicefordict.wav')
		os.system('pkill -CONT vlc')
		return 1

	elif((inp.find("quit",0,len(inp))!=-1) or (inp.find("exit",0,len(inp))!=-1)):
		os.system('pkill vlc')
		return 0

	else:
		os.system('pkill -STOP vlc')
		if(rand()==1):
			os.system('vlc --no-one-instance --play-and-exit else1.wav &')
		elif(rand()==2):
			os.system('vlc --no-one-instance --play-and-exit else2.wav &')
		elif(rand()==3):
			os.system('vlc --no-one-instance --play-and-exit else3.wav &')
		os.system('pkill -CONT vlc')
		return 1

def main():
	os.system('pkill -9 vlc')
	os.system("vlc --one-instance --play-and-exit win98startup.mp3")
	#readitaloud("Hello Welcome to the REASYS, your interactive reading assistant system to explore the pages of your favourite.Lets get started")
	os.system('vlc --one-instance --play-and-exit hellomessage.wav ')
	dictate=0
	val=1
	nfile=open("name.txt")
	nfile.seek(0)
	name=nfile.read(1)
	name1=nfile.read()
	nfile.close()
	if not name:
		if(rand()==1):
			readitaloud("Hello , i am your very friendly reading assistant... May i know your name")
		elif(rand()==2):
			readitaloud("Good day , Can i know your name.. please")
		else:
			readitaloud("Hi.. i am your virtual reading partner.. what is your good name?")


		os.system('python googlestt.py')
		src=open("s2t.txt")
		inpu=src.read()
		src.close()
		nfile=open("name.txt","r+")
		os.system(">name.txt")
		nfile.write(inpu)
		nfile.close()

	"""nfile1=open("name.txt")
	name1=nfile1.read()
	nfile.close()
	dest =  open("t2s.txt","r+")
	os.system(">t2s.txt")
	dest.write("Hello %s , i am your friendly reading assistant..\
	I can perform the following functions.I can dictate the book.\
	I can find you the definition of a word if you say define and then the word.\
	I can  "%name1)
	dest.close()
	os.system('python ibmwatsonforace.py')"""
	os.system('vlc  --one-instance --play-and-exit hellofunction.wav ')

	while(val!=0):
		os.system('python googlestt.py')
		src=open("s2t.txt")
		inp1= src.read()
		src.close()
		#if((inp1.find("okay",0,len(inp1))!=-1) and ((inp1.find("Google",0,len(inp1))!=-1) or (inp1.find("google",0,len(inp1))!=-1))):
			#print "this just in :P"
			#os.system('vlc-ctrl pause')
		#os.system('pkill -STOP vlc')
		#readitaloudforprompt("Yeah.. How can i be of service to you...")
			#os.system('python googlestt.py')
			#src=open("s2t.txt")
			#inp=src.read()
		inp1.lower()
			#src.close()
		os.system('pkill -CONT vlc')
		val=chat(inp1)


main()



