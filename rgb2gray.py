import cv2

def rgb2gray(image_path):
	"This function accepts path to an RGB image and converts it into a greyscale image and stores it as original_gray.jpg" 
	
	rgb_image = cv2.imread(image_path, -1)										#-1 flag means the image is opened as it is 			
	gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)					#converting the image into grayscale
	gray_path = image_path.replace('.jpg','_gray.jpg') 							#saving the image as original_gray.jpg
	print "Image has been converted into grayscale" 
	cv2.imwrite(gray_path, gray_image)                                             
