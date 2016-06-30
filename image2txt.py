import pytesseract
from PIL import Image

def image2txt(imagepath):
	"This function accepts path to a jpg image file , it does OCR on it using Google's Tesseract engine and writes the extracted data in a .txt file"
	
	text_out = imagepath.replace('.jpg', '.txt')							#Name of the text file will be same as the name of the image
	file_output = open(text_out, 'w')										#Opening a text file for writing
	file_output.write(pytesseract.image_to_string(Image.open(imagepath)))	#Writing the extracted text into the opened text file
	
	print "image to txt conversion is complete"
	
	#img = Image.open('/home/sherlock31/Desktop/Intern/testing_29june/15.tif')
	
		
	
	
