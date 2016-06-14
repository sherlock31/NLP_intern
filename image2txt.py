import pytesseract
from PIL import Image

def image2txt(imagepath):
	"This function accepts a jpg image file , it does OCR on it using Google's Tesseract engine and writes the extracted data in a .txt file"
	
	text_temp = imagepath.replace('.jpg','.txt')
	file_output = open(text_temp,'w')
	file_output.write(pytesseract.image_to_string(Image.open(imagepath)))
	print "image to txt conversion is complete"
	
		
	
	
