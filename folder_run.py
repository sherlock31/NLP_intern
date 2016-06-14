import os
from ocr import ocr

def folder_run(folder_path):
	"This function accepts path to a folder as input and runs the OCR function on all the files"
	for file_name in os.listdir(folder_path):
		ocr(f)
		
