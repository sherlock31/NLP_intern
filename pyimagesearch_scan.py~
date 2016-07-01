from skimage.filters import threshold_adaptive
import numpy as np
import cv2
from skimage import img_as_ubyte

def scan(image_path):
	
	image = cv2.imread(image_path)
	#ratio = image.shape[0] / 500.0
	#orig = image.copy()
	
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#	gray = cv2.GaussianBlur(gray, (5, 5), 0)
#	edged = cv2.Canny(gray, 75, 200)
#	print "STEP 1: Edge Detection"
#	cv2.imshow("Image", image)
#	cv2.imshow("Edged", edged)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()
	
	thresh = threshold_adaptive(gray, 251, offset = 10)
	thresh = img_as_ubyte(thresh)
	out_path = image_path.replace('.jpg','_thresh.jpg')
	cv2.imwrite(out_path, thresh)
