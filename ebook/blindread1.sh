#!/bin/bash
for i in {14..20}
do
	gs -sDEVICE=png16m -dINTERPOLATE -dFirstPage=$i -dLastPage=$i -r300 -o ./img$i -c 30000000 setvmthreshold -f Inferno.pdf

	./textcleaner.sh  img$i img21$i.jpg -g -e stretch -f 25 -o 20 -t 50 -u -s 1 -T -p 20
	#convert img2.jpg -crop 50%x100% +0 + 0 img.jpg
	convert img21$i.jpg  -resize 1500  -threshold 80% a$i.tif 
	tesseract a$i.tif  a$i 			
	#gedit b.txt
	#printf '%b\n' "$(cat a$i.txt)"	
	#festival --tts b.txt
	#python convert.py
	#python ibmwatson.py 			# accepts a text file and stores the STT of that text in the given path
done
python slice.py &					#allocates the text files a seperate folder and runs IBMwatson which splits a page into lines
#python play.py   




#-colorspace gray  +dither  -colors 2  -normalize 
#-morphology close square:1 
#-density 300  -depth 8 -background white