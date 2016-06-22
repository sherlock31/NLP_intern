import numpy as np
import cv2
from matplotlib import pyplot as plt

def pre_process_image(imagepath):
	"This function accepts path to an image as it's input and performs IP operations on it using opencv to preprocess it before performing OCR"

	img = cv2.imread(imagepath)												#/home/sherlock31/Desktop/Intern/Testing/labfiles-set1_0001.jpg
	improv_path =  imagepath.replace('.jpg', '_2.jpg')
	improved_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
	print "Noise removal is finished"
	
	
	
	
	
	cv2.imwrite(improv_path, improved_img)
	
