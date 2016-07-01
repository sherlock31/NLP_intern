import cv2

def rotate_image(image_path, angle):
	"This function accepts a path to an image and the angle of skew as input arguments and rotates the image by that angle using OpenCV"
	
	img = cv2.imread(image_path, -1)							#reading the image as it is 
	(h, w) = img.shape[:2]										#storing the size of the image
																				
	center = (w/2, h/2)											#center of the image 
	rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)		#rotational matrix
	rotated_img = cv2.warpAffine(img, rot_mat, (w,h))			#performing rotation
	rotated_path = image_path.replace('.jpg','_rotated.jpg') 	#name of the rotated image will be original_rotated.jpg
	print "Skew correction is finished"							
	
	#Let's crop the rotated image now or else black borders may be introduced which may hamper with OCR
	
	if angle > 0:													
		swap_variable = w
		w = h
		h = swap_variable
		
	cropped_image = cv2.getRectSubPix(rotated_img, (w, h), center)		#cropping the image 
	print "Cropping of rotated image is now finished"		
	cv2.imwrite(rotated_path, cropped_image)
