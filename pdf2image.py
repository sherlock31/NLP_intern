def pdf2image(filepath):
	"This function accepts a pdf file, it converts into a .jpg image using wand module"
	
	from wand.image import Image
	from wand.color import Color
	#from PIL import Image
	
	with Image(filename = filepath, resolution=200) as img:
		img.format = 'jpeg'
		img.compression_quality = 99
		img.save(filename='winter.jpg')
		
		
