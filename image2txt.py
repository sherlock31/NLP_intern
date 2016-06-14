def image2txt(filepath):
	"This function accepts a jpg image file , it does OCR on it using Google's Tesseract engine and returns a path to a.txt file"
	import pytesseract
	from PIL import Image
	file_output = open('text_output','w')
	file_output.write(pytesseract.image_to_string(Image.open(filepath)))
	
		
	
	
