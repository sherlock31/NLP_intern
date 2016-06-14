def ocr(filepath):
	"This function takes path to an a pdf file as output ,runs OCR on it using Google's Tesseract OCR engine and stores the textual data in a text file"
	pdf2image(filepath)
	image2txt(
