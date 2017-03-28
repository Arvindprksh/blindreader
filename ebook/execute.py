import os

def playSongsfromDirectory():
	os.chdir("/home/arvind/Desktop/project/tesseract_testing/ebook/")
	os.system('vlc -L "audio"')

def main():
	os.system("./blindread1.sh")
	#for i in range(14,16):
	#	os.chdir("/home/arvind/Desktop/project/tesseract_testing/ebook/%d/" %i)
	#	os.system("python ibmwatson.py")
	playSongsfromDirectory()

main()