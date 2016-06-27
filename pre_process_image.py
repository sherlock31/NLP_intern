import cv2
#from matplotlib import pyplot as plt
#from scipy import misc
#from scipy import ndimage
#import numpy as np
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
	rotated_path = gray_path.replace('.jpg', '_rotated.jpg')
	
	img = cv2.imread(rotated_path)
	improved_img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)    #Noise Removal
	
	improv_path =  rotated_path.replace('.jpg', '_improved.jpg')
	cv2.imwrite(improv_path, improved_img)
	
