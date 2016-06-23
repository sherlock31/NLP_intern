import cv2
import numpy as np
from math import atan2

def deskew(image_path):
	"This function accepts path to an image, finds it's skew angle and deskews it using OpenCV"
	
	img_temp = cv2.imread(image_path)
	gray_temp = cv2.cvtColor(img_temp,cv2.COLOR_BGR2GRAY)				#Converting it into grayscale
	#edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
	invert_temp = 255 - gray_temp									#inverting the image
	minLineLength = 50												#make them a function of image dimensions if possible
	maxLineGap = 10

	lines_temp = cv2.HoughLinesP(invert_temp, 1, np.pi/180, 100, minLineLength, maxLineGap)		#Probabilistic Hough transform 

	angle_temp = 0.0
	for i in range(1, lines_temp.shape[0]):
		angle_temp = angle_temp + atan2((float(lines_temp[i][0][3]) - float(lines_temp[i][0][1])), (float(lines_temp[i][0][2]) - float(lines_temp[i][0][0])))
	
	angle_temp = float(angle_temp) / float(lines_temp.shape[0]) 			#Beware! angle is in RADIANS
	angle_temp = float(angle_temp)*180.0/float(np.pi)		#Now it's in DEGREES
	print "Angle of skew is:"
	print angle_temp
	
	#Let's rotate the image based on the angle now!
	(h_temp,w_temp) = img_temp.shape[:2]
	center_temp = (w_temp/2, h_temp/2)
	rot_mat_temp = cv2.getRotationMatrix2D(center_temp, angle_temp, 1.0)
	rotated_img_temp = cv2.warpAffine(img_temp, rot_mat_temp, (w_temp,h_temp))#Some problem in types of arguments, changed the name of all the variables
	rot_path_temp = image_path.replace('.jpg', '_rot.jpg')
	cv2.imwrite(rot_path_temp, rotated_img_temp)
