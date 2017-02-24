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
		os.system('cvlc --play-and-exit output_en-US_AllisonVoice.wav &')
		os.system('./blindread1.sh ')
		return 1
	elif((inp.find("stop",0,len(inp))!=-1) and (inp.find("book",0,len(inp))!=-1)):
		dest = open("t2s.txt",'r+')
		os.system(">t2s.txt")
		dest.write("ok.. i guess thats it for today")
		dest.close()
		os.system('python ibmwatsonforace.py')
		os.system('cvlc --play-and-exit output_en-US_AllisonVoice.wav')
		return 1
	elif((inp.find("define",0,len(inp))!=-1) or (inp.find("definition",0,len(inp))!=-1)):
		print "ok"
		dest = open("txt1.txt",'r+')
		os.system(">txt1.txt")
		dest.write(inp)
		dest.close()
		os.system('python pydictionary1.py')
		os.system('python ibmwatsonforace.py')
		os.system('cvlc --play-and-exit output_en-US_AllisonVoice.wav')
		return 1

val=1
while(val!=0):
	os.system('python googlestt.py')
	src=open("s2t.txt")
	inp=src.read()
	src.close()
	val=chat(inp)