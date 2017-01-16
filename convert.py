import sys
import os
import codecs

filePath = "b.txt"
fichier = codecs.open(filePath,"r", encoding ="utf-8")
contentOfFile = fichier.read()
fichier.close()

fichierTemp = codecs.open("b.txt" , "w", encoding="ascii", errors="ignore")
fichierTemp.write(contentOfFile)
fichierTemp.close()