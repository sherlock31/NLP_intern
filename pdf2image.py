def pdf2image(filepath):
	"This function accepts a pdf file, it converts into a .jpg image using wand module"
	from wand.image import Image
	from wand.color import Color
	#from PIL import Image
	
	with Image(filename = filepath, resolution=200) as image:
	    image.compression_quality = 99
        image.save(filename='image_pdf.jpg')
		
		
