import cv2
import numpy as np

def sharpen(image_path):
	
	img = cv2.imread(image_path)
	kernel_sharpen_3 = (np.array([[-1,-1,-1,-1,-1],
                             	  [-1,2,2,2,-1],
                                  [-1,2,8,2,-1],
                                  [-1,2,2,2,-1],
                                  [-1,-1,-1,-1,-1]]) / 8.0)
                             
    out_img = cv2.filter2D(img, -1, kernel_sharpen_3)
    out_path = image_path.replace('.jpg', '_sharpened.jpg')
    cv2.imwrite(out_path, out_img)
