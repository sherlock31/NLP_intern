import numpy as np
import cv2
from matplotlib import pyplot as plt
from calc_angle import calc_angle
from rotate_image import rotate_image

def pre_process_image(imagepath):
	"This function accepts path to an image as it's input and performs IP operations on it using OpenCV to preprocess it before performing OCR"
	
	angle_rot = calc_angle(imagepath)										#calculate skew angle 
	img = rotate_image(imagepath, angle_rot)								#passing the imagepath and skew angle to rotate_image to correct the skew	
	img = 255 - img
	improved_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)#Noise Removal
	print "Noise removal is finished"
	improv_path =  imagepath.replace('.jpg', '_improved_without_nr.jpg')
	cv2.imwrite(improv_path, improved_img)
	
