import numpy as np
from scipy import signal
from PIL import Image

def denoise(image_path):
	"This function accepts path to an image, does noise correction on it using medfilter and stores the corrected image"
	
	inp_img = np.asarray(Image.open(image_path))/255.0
	
	background_img = signal.medfilt2d(inp_img, 11)
	back_tmp = np.asarray(background_img * 255.0, dtype = np.uint8)
	back_path = image_path.replace('.jpg', '_background.jpg')
	#Image.fromarray(back_tmp).save(back_path)
	
	mask_img = inp_img < background_img - 0.1
	mask_tmp = np.asarray(mask_img * 255.0, dtype = np.uint8)
	mask_path = image_path.replace('.jpg', '_foreground_mask.jpg')
	#Image.fromarray(mask_tmp).save(mask_path)
	
	out_img = np.where(mask_img, inp_img, 1.0)
	out_tmp = np.asarray(out_img * 255.0, dtype = np.uint8)
	out_path = image_path.replace('.jpg', '_denoised.jpg') 
	Image.fromarray(out_tmp).save(out_path)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
