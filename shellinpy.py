import os
def REASYS:
	os.system('./textcleaner.sh  img2.jpg img21.jpg -g -e stretch -f 25 -o 20 -t 50 -u -s 1 -T -p 20')
	os.system('convert img21.jpg  -resize 2000  -morphology close square:1 -threshold 90%  a.tif')
	os.system('tesseract a.tif b')
	os.system('python ibmwatson.py')
	os.system('cvlc output_en-US_AllisonVoice.wav')
