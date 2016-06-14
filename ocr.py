from pdf2image import pdf2image
from image2txt import image2txt	

def ocr(filepath):
	"This function takes path to an a pdf file as output ,runs OCR on it using Google's Tesseract OCR engine and stores the textual data in a text file"
	pdf2image(filepath)
	image_path = filepath.replace('.pdf', '.jpg')
	image2txt(image_path)
	print "OCR is finished successfully"
