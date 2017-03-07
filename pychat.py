import os
import time
def readitaloud(string):
	dest = open("t2s.txt",'r+')
	os.system(">t2s.txt")
	dest.write(string)
	dest.close()
	os.system('python ibmwatsonforace.py')
	os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav')

def chat(inp):
	if((inp.find("start",0,len(inp))!=-1) and (inp.find("reading",0,len(inp))!=-1)):
		readitaloud("Ok... lets start reading the book")
		os.system("./blindread1.sh")
		return 1
	elif((inp.find("pause",0,len(inp))!=-1) or (inp.find("hold",0,len(inp))!=-1)):
		#readitaloud("Ok... lets pause right here.. we will be back whenever you want")
		os.system('pkill -STOP vlc')
		return 1
	elif((inp.find("continue",0,len(inp))!=-1) or (inp.find("resume",0,len(inp))!=-1)):
		#readitaloud("Right.. Shall we begin now..")
		os.system('pkill -CONT vlc')
		return 1

	elif((inp.find("stop",0,len(inp))!=-1) and (inp.find("book",0,len(inp))!=-1)):
		os.system('pkill vlc')
		readitaloud("ok.. i guess thats it for today")
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
		os.system('vlc --play-and-exit output_en-US_AllisonVoicefordict.wav')
		os.system('pkill -CONT vlc')
		return 1

	elif((inp.find("quit",0,len(inp))!=-1) or (inp.find("exit",0,len(inp))!=-1)):
		os.system('pkill vlc')
		return 0

	else:
		os.system('pkill -STOP vlc')
		readitaloud("i am sorry can you repeat what you just said")
		os.system('pkill -CONT vlc')
		return 1

val=1
nfile=open("name.txt")
nfile.seek(0)
name=nfile.read(1)
name1=nfile.read()
nfile.close()
if not name:
	readitaloud("Hello , i am your very friendly reading assistant... May i know your name")
	os.system('python googlestt.py')
	src=open("s2t.txt")
	inpu=src.read()
	src.close()
	#print inpu
	nfile=open("name.txt","r+")
	os.system(">name.txt")
	nfile.write(inpu)
	nfile.close()

nfile1=open("name.txt")
name1=nfile1.read()
nfile.close()
dest =  open("t2s.txt","r+")
os.system(">t2s.txt")
dest.write("Hello %s , i am your friendly reading assistant.. How can i be of service to you.." %name1)
dest.close()
os.system('python ibmwatsonforace.py')
os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav &')

while(val!=0):
	os.system('python googlestt.py')
	src=open("s2t.txt")
	inp=src.read()
	src.close()
	val=chat(inp)