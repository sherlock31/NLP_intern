import numpy as np
import cv2
from matplotlib import pyplot as plt

def pre_process_image(imagepath):
"This function accepts path to an image as it's input and performs IP operations on it using opencv to preprocess it before performing OCR"
#/home/sherlock31/Desktop/Intern/Testing/labfiles-set1_0001.jpg
	img = cv2.imread(imagepath)
	improv_path =  imagepath.replace('.jpg', '.png')
	improved_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	cv2.imwsrite(improv_path, improved_img)
	
