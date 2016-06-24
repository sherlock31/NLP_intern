import numpy as np
from skimage.transform import radon
from PIL import Image
from numpy import asarray, mean, array, blackman
import numpy
from numpy.fft import rfft
import matplotlib.pyplot as plt
from matplotlib.mlab import rms_flat

try:
    from parabolic import parabolic
    def argmax(x):
        return parabolic(x, numpy.argmax(x))[0]
except ImportError:
    from numpy import argmax


def calc_angle(image_path):
	"This function accepts path to an image and find it's skew angle using Radon Transform"
	
	img = Image.open(image_path)														#opening the image 
	(h, w) = img.size																	#finding the size of the image 
	
	if h>1000: (h, w) = (int(h/10), int(w/10))											#reducing the size if the image is too big to increase the speed

	img = img.resize((h,w), Image.ANTIALIAS)					
	I = asarray(img.convert('L'))
	I = I - mean(I)  																	# Demean; make the brightness extend above and below zero

# Do the radon transform and display the result
	sinogram = radon(I)
# Find the RMS value of each row and find "busiest" rotation,
# where the transform is lined up perfectly with the alternating dark
# text and white lines
	r = array([rms_flat(line) for line in sinogram.transpose()])
	rotation = argmax(r)

	print("skew angle detection is finished")
	return (90 - rotation)
	
