import cv2
import numpy as np
from math import atan2

def deskew(image_path):
	
	img = cv2.imread(image_path)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
	invert = 255 - gray
	minLineLength = 50
	maxLineGap = 10

	lines = cv2.HoughLinesP(invert, 1, np.pi/180, 100, minLineLength, maxLineGap)

	angle = 0.0
	for i in range(1, lines.shape[0]):
		angle = angle + atan2((float(lines[i][0][3]) - float(lines[i][0][1])), (float(lines[i][0][2]) - float(lines[i][0][0])))
	
	angle = float(angle) / float(lines.shape[0]) 			#Beware! angle is in RADIANS
	angle = float(angle)*180.0/float(np.pi)		#Now it's in DEGREES
	print "Angle of skew is:"
	print angle*180/np.pi
	
	#Let's rotate the image based on the angle now!
	(h,w) = img.shape[:2]
	center = (w/2, h/2)
	rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
	rotated_img = cv.warpAffine(img, rot_mat, img.size(), INTER_CUBIC)
	rot_path = image_path.replace('.jpg', '_rot.jpg')
	cv2.imwrite(rot_path, rotated_img)
