import os
import time

def chat(inp):
	#print inp
	print inp.find("start",0,len(inp))
	print inp.find("reading",0,len(inp))
	print inp.find("stop",0,len(inp))
	print inp.find("reading",0,len(inp))
	if((inp.find("start",0,len(inp))!=-1) and (inp.find("reading",0,len(inp))!=-1)):
		dest = open("t2s.txt",'r+')
		os.system(">t2s.txt")
		dest.write("Ok... lets start reading the book")
		dest.close()
		os.system('python ibmwatsonforace.py')
		os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav &')
		os.system('./blindread1.sh ')
		return 1
	elif((inp.find("pause",0,len(inp))!=-1) or (inp.find("hold",0,len(inp))!=-1)):
		"""dest = open("t2s.txt",'r+')
		os.system(">t2s.txt")
		dest.write("Ok... lets pause right here.. we will be back whenever you want")
		dest.close()
		os.system('pkill -9 vlc')
		os.system('python ibmwatsonforace.py')
		os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav &')"""
		os.system('pkill -STOP vlc')
		return 1
	elif((inp.find("continue",0,len(inp))!=-1) or (inp.find("resume",0,len(inp))!=-1)):
		"""dest = open("t2s.txt",'r+')
		os.system(">t2s.txt")
		dest.write("Right.. Shall we begin now..")
		dest.close()
		os.system('python ibmwatsonforace.py')
		os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav &')"""
		os.system('pkill -CONT vlc')
		return 1
	elif((inp.find("stop",0,len(inp))!=-1) and (inp.find("book",0,len(inp))!=-1)):
		os.system('pkill vlc')
		dest = open("t2s.txt",'r+')
		os.system(">t2s.txt")
		dest.write("ok.. i guess thats it for today")
		dest.close()
		os.system('python ibmwatsonforace.py')
		os.system('vlc --play-and-exit output_en-US_AllisonVoiceforace.wav')
		
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
		return 0

val=1
while(val!=0):
	os.system('python googlestt.py')
	src=open("s2t.txt")
	inp=src.read()
	src.close()
	val=chat(inp)