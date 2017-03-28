import os
a=open("length.txt")
leng=int(a.read())
a.close()
re=open("rewindflag.txt")
n1=re.read()
n=int(n1)
print n
c=0
print os.getcwd()
a="vlc --play-and-exit -L"
print leng
if(n==0):
	for i in range(int(leng)):
		if(os.path.isfile("output_en-US_AllisonVoice%d.wav" %i) == False or os.stat("b%d.txt" %i).st_size == 0): 
			continue
		else:
			a=a+" output_en-US_AllisonVoice%d.wav" %i
	print a
	os.system(a)
elif(n==1):
	for i in range(2):
		os.system('vlc-ctrl prev &')
"""
    elif(n==1):
    	print "hello"
        b=open('count.txt'
        j=b.read() 
        i=int(j)-2;
        if(i==int(j)-2):
        	os.system('vlc --play-and-exit output_en-US_AllisonVoice0.wav ')
        else:
        	os.system('vlc --play-and-exit --one-instance --playlist-enqueue output_en-US_AllisonVoice%d.wav ' %i)
"""