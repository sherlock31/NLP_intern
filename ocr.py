from pdf2image import pdf2image
from image2txt import image2txt	
from pre_process_image import pre_process_image
import os																		
import shutil																	
from pyPdf import PdfFileReader
import pytesseract
from PIL import Image

def ocr(filepath):
	"This function takes path to an a pdf file as output, runs OCR on it using Google's Tesseract OCR engine and stores the textual data in a text file"
	
	pdf = PdfFileReader(open(filepath))							#reading the PDF
	pages = pdf.getNumPages()									#no. of pages in the PDF
	
	new_folder_path = filepath[:-4]								#removing ".pdf" from the filepath
	os.makedirs(new_folder_path)								#make a new folder for the pdf, name of the folder will be same as that of the pdf
	shutil.move(filepath, new_folder_path)						#pdf is moved to the newly created of the same name 
	
	name_of_pdf = ""
	for w in reversed(filepath):								#to find the name of the pdf from the path 
		if(w == '/'):
			break
		else:
			 = name_of_pdf + w									#name_of_pdf stores the name of the pdf(reversed)
			
	name_of_pdf = name_of_pdf[::-1]								#reversing the name of the pdf as it was originally reversed
	
	new_path_to_file = new_folder_path + name_of_pdf			#the complete path to the PDF 
	pdf2image(new_path_to_file)									#Conversion of PDF into an image 
	
	list_of_images = []																			
	if (pages > 1):
		for i in range(0,pages):
			temp =  name_of_pdf[:-4] + "-" + str(i) + ".jpg" 		#conversion to the naming convention in which the converted images are stored 
			new_path_to_image = new_folder_path + temp 				
			list_of_images.append(temp)								#making a list in which all the names of all the converted images will be stored 
			pre_process_image(new_path_to_image)					#preprocess all the images created from the pdf
			
	else:
		pre_process_image(new_folder_path + name_of_pdf[:-4] + ".jpg")	#If there is only one page 
	
	#improv_path =  image_path.replace('.jpg', '_gray_rotated_improved.jpg')
	
#Now we have images with names orig-no._gray_rotated_improved.jpg, so we need to extract out the textual data from them and join them in a single text file
	
	if (pages == 1):
		image2txt(new_folder_path + name_of_pdf[:-4] + "_gray_rotated_improved.jpg")
		print "OCR is finished successfully"
	
	
	else:
		textual_data = ""
		file_output = open(text_temp, 'w'
		
		for l in list_of_images:
			temp_path = new_folder_path + l			#path to the lth image 
			textual_data += pytesseract.image_to_string(Image.open(temp_path)	
		
		file_output.write(textual_data)
		print "OCR is finished successfully"
					
	
	
