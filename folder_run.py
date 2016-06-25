import os
#from ocr import ocr
#from pdf2image import pdf2image
#from calc_angle import calc_angle
#from rotate_image import rotate_image
#from denoise_kaggle import denoise 
#from rgb2gray import rgb2gray
from image2txt import image2txt

def folder_run(folder_path):
	"This function accepts path to a folder as input and runs the OCR function on all the files"
	for file_name in os.listdir(folder_path):
		#angle_rot = calc_angle(folder_path + "/" + file_name)
		#rotate_image(folder_path + "/" + file_name, angle_rot)
		#denoise(folder_path + "/" + file_name)
		#rgb2gray(folder_path + "/" + file_name)
		image2txt(folder_path + "/" + file_name)
