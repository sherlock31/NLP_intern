from wand.image import Image
from wand.color import Color
	
def pdf2image(filepath):
	"This function accepts a pdf file, it converts into a .jpg image using wand module"
	
	image_path = filepath.replace('.pdf','.jpg')				#Name of the image that will be saved will be same as the name of the pdf			
	
	with Image(filename = filepath, resolution = 400) as img:	#resolution is 400 DPI
		img.format = 'jpeg'										#image format will be jpeg
		img.compression_quality = 99							#compression quality
		img.save(filename = image_path)							#saving the image as jpeg
		print "PDF has been converted into an image"			
		
		
