import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path
def main():
	for i in range(14,16):
		os.system("mkdir -p %d" %i)
		os.system("cp /home/arvind/Desktop/project/tesseract_testing/ebook/a%d.txt  /home/arvind/Desktop/project/tesseract_testing/ebook/%d/b.txt" %(i,i))		
		os.system("cp /home/arvind/Desktop/project/tesseract_testing/ebook/ibmwatson.py  /home/arvind/Desktop/project/tesseract_testing/ebook/%d/" %i)
		os.system("cp /home/arvind/Desktop/project/tesseract_testing/ebook/ibmwatsonforace.py  /home/arvind/Desktop/project/tesseract_testing/ebook/%d/" %i)
		os.system("cp /home/arvind/Desktop/project/tesseract_testing/ebook/ibmwatsonforprompt.py  /home/arvind/Desktop/project/tesseract_testing/ebook/%d/" %i)
		os.system("cp /home/arvind/Desktop/project/tesseract_testing/ebook/sentsplit.py  /home/arvind/Desktop/project/tesseract_testing/ebook/%d/" %i)			
main()