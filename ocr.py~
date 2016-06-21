from pdf2image import pdf2image
from image2txt import image2txt	
from pre_process_image import pre_process_image

def ocr(filepath):
	"This function takes path to an a pdf file as output ,runs OCR on it using Google's Tesseract OCR engine and stores the textual data in a text file"
	pdf2image(filepath)
	image_path = filepath.replace('.pdf', '.jpg')		#Name of the image that will be saved will be same as the name of the pdf
	pre_process_image(image_path)
	improv_path =  image_path.replace('.jpg', '_2.jpg')
	
	image2txt(improv_path)								#/home/sherlock31/Desktop/Intern/Testing/labfiles-set1_0027.pdf
	print "OCR is finished successfully"
