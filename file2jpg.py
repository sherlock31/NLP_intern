from wand.image import Image
from wand.color import Color
	
def file2jpg(filepath):
	"This function accepts a pdf file, it converts into a .jpg image using wand module"
	
	file_type = ''
	for w in reversed(filepath):			
		if(w == '.'):
			break
		else
			file_type = file_type + w				
			
	file_type = file_type[::-1]									#filetype now stores the file extension of the file 
	image_path = filepath.replace(file_type,'.jpg')				#Name of the image that will be saved will be same as the name of the pdf			
	
	with Image(filename = filepath, resolution = 400) as img:	#resolution is 400 DPI
		img.format = 'jpeg'										#image format will be jpeg
		img.compression_quality = 99							#compression quality
		img.save(filename = image_path)							#saving the image as jpeg
		print "File has been converted into an JPEG image"			
		
		
