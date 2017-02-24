import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()
ar=open("txt1.txt")
tex=ar.read()
print tex
inpwords = tex.split()
print inpwords
c=open("t2s.txt","r+")
os.system('>t2s.txt')
text=dictionary.meaning(inpwords[1])
c.write(str(text))