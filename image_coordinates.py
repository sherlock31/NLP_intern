from pytesseract import pytesseract
from bs4 import BeautifulSoup

def image_coordinates(image_path):
	"This function accepts path to an image, it will use pytesseract and Beautiful Soup to extract out the coordinates of the identified characters in the image "
	
	output_path = image_path[:-4]				
	text_path  =image_path.replace('.jpg', '_char_coord.txt')
	f = open(text_path, 'w')
	
	pytesseract.run_tesseract(image_path, output_path, lang = None, boxes = False, config = "hocr")		#a hocr file with image's name will be created 
	output_path = output_path + ".hocr"
	image_soup = BeautifulSoup(open(output_path))				#opening the .hocr file to extract the bounding box coordinates
	str_image_soup = str(image_soup)							#converting the soup object into string to extract out data
	word_count = str_image_soup.count("word_")					#number of elements with id word_some_number, which is basically the number
	
	for i in range(1, word_count + 1):
		
		str_temp = str(image_soup.find_all(id="word_1_"+ str(i)))
		start_point = int(str_temp.find("<em>"))				#index of '<' in <em> tag
		start_point += 4										#index of the word that it it contains 		
		end_point = int(str_temp.find("</em>"))					#index of '<' in </em> tag
		word = str_temp[start_point:end_point]				
		
		#if(not (word == '')):												#if word is not empty 
		start_point = int(str_temp.find("bbox"))				
		start_point += 5
		end_point = int(str_temp.find(";"))
		bounding_box = str_temp[start_point:end_point]			
		f.write(word + " " + bounding_box + "\n")
		
	
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
