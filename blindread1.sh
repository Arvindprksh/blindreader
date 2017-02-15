#!/bin/bash
./textcleaner.sh  img2.jpg img21.jpg -g -e stretch -f 25 -o 20 -t 50 -u -s 1 -T -p 20
#convert img2.jpg -crop 50%x100% +0 + 0 img.jpg
convert img21.jpg  -resize 2000  -morphology close square:1 -threshold 90% a.tif 
tesseract a.tif  b 
#gedit b.txt
printf '%b\n' "$(cat b.txt)"
#festival --tts b.txt
#python convert.py
python ibmwatson.py
cvlc output_en-US_AllisonVoice.wav 
#-colorspace gray  +dither  -colors 2  -normalize 
#-threshold 80%