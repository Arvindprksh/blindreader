import os
import time
import math
import random
flag = 0
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
	if((inp.find("start",0,len(inp))!=-1) or (inp.find("begin",0,len(inp))!=-1) ):
		flag=1
		re=open("rewindflag.txt","r+")
		os.system(">rewindflag.txt")
		re.write("0")
		if(rand()==1):
			readitaloud("Ok... lets start reading the book")
		elif(rand()==2):
			readitaloud("Fine... shall we begin to read the book")
		elif(rand()==3):
			readitaloud("Cool.. Lets read the book")

		os.system("python execute.py &")
		return 1

	elif((inp.find("pause",0,len(inp))!=-1) or (inp.find("hold",0,len(inp))!=-1)):
		#readitaloud("Ok... lets pause right here.. we will be back whenever you want")
		print "pause is working"
		os.system('pkill -STOP vlc')
		return 1
	elif((inp.find("continue",0,len(inp))!=-1) or (inp.find("resume",0,len(inp))!=-1)):
		#readitaloud("Right.. Shall we begin now..")
		print "continue is working"
		os.system('pkill -CONT vlc')
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
		if(rand()==1):
			readitaloud("ok.. i guess thats it for today")
		elif(rand()==2):
			readitaloud("Cool... lets wrap this up..")
		elif(rand()==3):
			readitaloud("Let's call it a day then..")
		os.system('pkill -9 vlc')
		return 1


	elif((inp.find("define",0,len(inp))!=-1) or (inp.find("definition",0,len(inp))!=-1)):
		print "ok"
		dest = open("dict.txt",'r+')
		os.system(">dict.txt")
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
			readitaloudforprompt("i am sorry can you repeat what you just said")
		elif(rand()==2):
			readitaloudforprompt("Sorry, but i didnt get you.. can you come again?")
		elif(rand()==3):
			readitaloudforprompt("ummm.. excuse me but i couldn't follow you.. come again?")
		os.system('pkill -CONT vlc')
		return 1

def main():
	os.system('pkill -9 vlc')
	os.system('vlc --one-instance --play-and-exit win98startup.mp3') 
	os.system('vlc --one-instance --play-and-exit Bleep.wav')
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

	nfile1=open("name.txt")
	name1=nfile1.read()
	nfile.close()
	dest =  open("t2s.txt","r+")
	os.system(">t2s.txt")
	dest.write("Hello %s , i am your friendly reading assistant..\
	I can perform the following functions.I can dictate the book.\
	I can find you the definition of a word if you say define and then the word.\
	I can  "%name1)
	dest.close()
	os.system('python ibmwatsonforace.py')
	os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav &')
	dictateInput=googleread()
	if((inp1.find("okay",0,len(inp1))!=-1) and (inp1.find("dictate",0,len(inp1))!=-1))
		readitaloud("What is the name of the book , you want to read?")
		bookName=googleread()
		if(os.path.isdir("%s" %bookName)):
			print "the book exists.What shall we do?"
		else:
			book=open("book.txt","r+")
			os.system(">book.txt")
			book.write("%s" %bookName)
			os.system("mkdir %s" %bookName)

		os.chdir("%s" %bookName)

		
		while(val!=0):
			os.system('python googlestt.py')
			src=open("s2t.txt")
			inp1=src.read()
			src.close()
			if((inp1.find("okay",0,len(inp1))!=-1) and ((inp1.find("Google",0,len(inp1))!=-1) or (inp1.find("google",0,len(inp1))!=-1))):
				print "this just in :P"
				#os.system('vlc-ctrl pause')
				os.system('pkill -STOP vlc')
				readitaloudforprompt("Yeah.. How can i be of service to you...")
				os.system('python googlestt.py')
				src=open("s2t.txt")
				inp=src.read()
				src.close()
				os.system('pkill -CONT vlc')
				val=chat(inp)


main()



