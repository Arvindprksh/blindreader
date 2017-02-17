import os
def chat(inp):
	print inp
	dest = open("t2s.txt",'r+')
	print inp.find("hi",0,len(inp))
	print inp.find("hello",0,len(inp))
	print inp.find("what",0,len(inp))
	print inp.find("doing",0,len(inp))
	if((inp.find("hi",0,len(inp))!=-1) or (inp.find("hello",0,len(inp))!=-1)):
		dest = open("t2s.txt",'r+')
		dest.write("Hello how are you.. i m fine and well")
		os.system('python ibmwatson.py')
		os.system('cvlc output_en-US_AllisonVoice.wav')
		dest.close()
		return 1
	elif((inp.find("what",0,len(inp))!=-1) and (inp.find("doing",0,len(inp))!=-1)):
		print "hello"
		dest = open("t2s.txt",'r+')
		dest.write("i am just processing billions of data.. what about you")
		os.system('python ibmwatson.py')
		os.system('cvlc output_en-US_AllisonVoice.wav')
		dest.close()
		return 0

val=1
while(val!=0):
	os.system('python googlestt.py')
	src=open("s2t.txt")
	inp=src.read()
	src.close()
	val=chat(inp)
os.system("exit()")
