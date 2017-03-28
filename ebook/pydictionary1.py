import os 
from PyDictionary import PyDictionary
dictionary=PyDictionary()
ar=open("dict.txt")
tex=ar.read()
inpwords = tex.split()
c=open("t2sfordict.txt","r+")
os.system('>t2sfordict.txt')
text=dictionary.meaning(inpwords[1])
c.write(str(text))