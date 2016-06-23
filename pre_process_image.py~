import numpy as np
import cv2
from matplotlib import pyplot as plt
from deskew import deskew 

def pre_process_image(imagepath):
	"This function accepts path to an image as it's input and performs IP operations on it using OpenCV to preprocess it before performing OCR"

	img = cv2.imread(imagepath)											
	improv_path =  imagepath.replace('.jpg', '_improved.jpg')
	improved_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)				#Noise Removal
	print "Noise removal is finished"
	
	rot_improv_img = deskew(improved_img)		
	
	
	
	
	cv2.imwrite(improv_path, rot_improv_img)
	
