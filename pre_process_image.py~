import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import misc
from scipy import ndimage
import numpy as np
from calc_angle import calc_angle
from rotate_image import rotate_image
from rgb2gray import rgb2gray 
#from skimage.filters import threshold_adaptive

def pre_process_image(image_path):
	"This function accepts path to an image as it's input and performs IP operations on it using OpenCV to preprocess it before performing OCR"
	
	rgb2gray(image_path)										#The RGB image will be changed into true grayscale, name will be changed to orig_gray.jpg
	gray_path = image_path.replace('.jpg', '_gray.jpg')			#path to the grayscale image 
	
	angle_rot = calc_angle(gray_path)							#calculate skew angle 
	rotate_image(gray_path, angle_rot)							#passing the image_path and skew angle to rotate_image to correct the skew	
	
	#improved_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)#Noise Removal
	
	#path_to_rotated_image = image_path.replace('.jpg', '_rotated.jpg')
	
	#print "Noise removal is finished"
	
	#Sharpeing the image using scipy
	
#	rot_img = misc.imread(path_to_rotated_image, flatten = True)	#tuning of the parameters may be required
#	blurred_img = ndimage.gaussian_filter(rot_img, 3)
#	filter_blurred_img = ndimage.gaussian_filter(blurred_img, 1)
#	alpha = 30
#	sharpened_img = blurred_img + alpha*(blurred_img-filter_blurred_img)
#	sharpened_path = image_path.replace('.jpg', '_sharp.jpg')
#	cv2.imwrite(sharpened_path, sharpened_img)
#	
	#Let's apply adaptive thresholding 
	#convert sharpened_img to greyscale through opencv functions :'(
	
#	thresh_img = cv2.adaptiveThreshold(sharpened_img, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#	
#	threshold_path = image_path.replace('.jpg', '_sharpened.jpg') 
#	cv2.imwrite(threshold_path, thresh_img)
	
	
	
	
#	improv_path =  image_path.replace('.jpg', '_improved.jpg')
#	cv2.imwrite(improv_path, improved_img)
	
