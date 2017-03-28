import os

file=open("b.txt")
words=file.read()
sentences=words.split('.')
file.close()

os.system('touch length.txt')
l=open("length.txt","r+")
os.system(">length.txt")
l.write(str(len(sentences)))


c=[0]*len(sentences)
#print len(sentences),sentences
for i in range(len(sentences)):
	os.system('touch b%d.txt' %i)
	c[i]=open("b%d.txt" %i ,"r+")
	os.system(">b%d.txt" %i)
	c[i].write(sentences[i])
	c[i].close()