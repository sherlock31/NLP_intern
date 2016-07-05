from file2image import file2image
from image2txt import image2txt 
from pre_process_image import pre_process_image
import os                                                                       
import shutil                                                                   
from pyPdf import PdfFileReader
import pytesseract
from PIL import Image
from docx import *
import sys 
def ocr(filepath):
    "This function takes path to a input file as output, runs OCR on it using Google's Tesseract OCR engine and stores the textual data in a text file"
    
    if(filepath.endswith('.pdf')):                                      #If it's a pdf file 
    
        new_folder_path = filepath[:-4]                                 #removing ".pdf" from the filepath
        os.makedirs(new_folder_path)                                    #make a new folder for the pdf, name of the folder will be same as that of the pdf
        shutil.move(filepath, new_folder_path)                          #pdf is moved to the newly created folder of the same name 
    
        name_of_pdf = ""
    
        for w in reversed(filepath):                                    #to find the name of the pdf from the path 
            if(w == '/'):
                break
            else:
                name_of_pdf = name_of_pdf + w                           #name_of_pdf stores the name of the pdf(reversed)
                
        name_of_pdf = name_of_pdf[::-1]                                 #reversing the name of the pdf as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_pdf          #the complete path to the PDF
        pdf = PdfFileReader(open(new_path_to_file))                     #reading the PDF
        pages = pdf.getNumPages()                                       #no. of pages in the PDF
    
        
         
        file2image(new_path_to_file)                                    #Conversion of PDF into an image 
    
        list_of_images = []                                                                         
        if (pages > 1):
            for i in range(0, pages):
                temp =  name_of_pdf[:-4] + "-" + str(i) + ".jpg"            #conversion to the naming convention in which the converted images are stored 
                new_path_to_image = new_folder_path + "/" + temp                
                list_of_images.append(temp)                                 #making a list in which all the names of all the converted images will be stored 
                pre_process_image(new_path_to_image)                        #preprocess all the images created from the pdf
            
        else:                                                               #If there is only one page 
            image_path = new_folder_path + "/"+ name_of_pdf[:-4] + ".jpg"
            pre_process_image(image_path)   
    
        if (pages == 1):
            image2txt(new_folder_path + "/" + name_of_pdf[:-4] + "_gray_rotated_improved.jpg")
            print "OCR is finished successfully"
    
    
        else:
            textual_data = ''
            text_path = new_folder_path + "/" + name_of_pdf[:-4] + '.txt'
            file_output = open(text_path, 'w')
        
            for l in list_of_images:
                temp_path = new_folder_path + "/" + l                               
                textual_data += pytesseract.image_to_string(Image.open(temp_path))
        
            file_output.write(textual_data)
            print "OCR is finished successfully"
            
    elif(filepath.endswith('.jpg')):                                    #If the input file is a .jpg image 
        new_folder_path = filepath[:-4] 
        os.makedirs(new_folder_path)                                    #make a new folder for the jpg, name of the folder will be same as that of the jpg
        shutil.move(filepath, new_folder_path)                          #jpg is moved to the newly created of the same name 
        
        name_of_image = ""
    
        for w in reversed(filepath):                                    #to find the name of the image from the path 
            if(w == '/'):
                break
            else:
                 name_of_image= name_of_image + w                       #name_of_image stores the name of the image(reversed)
                
        name_of_image = name_of_image[::-1]                             #reversing the name of the image as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_image        #the complete path to the image 
        pre_process_image(new_path_to_file)                             #preprocessing the image 
        
        image2txt(new_folder_path + "/" + name_of_image[:-4] + "_gray_rotated_improved.jpg")
        print "OCR is finished successfully"
        
    elif(filepath.endswith('.tiff')):                                   #If the input file is a .tiff image 
        new_folder_path = filepath[:-5] 
        os.makedirs(new_folder_path)                                    #make a new folder for the tiff, name of the folder will be same as that of the tiff
        shutil.move(filepath, new_folder_path)                          #tiff is moved to the newly created of the same name 
        
        name_of_image = ""
    
        for w in reversed(filepath):                                    #to find the name of the image from the path 
            if(w == '/'):
                break
            else:
                 name_of_image = name_of_image + w                      #name_of_image stores the name of the image(reversed)
                
        name_of_image = name_of_image[::-1]                             #reversing the name of the image as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_image        #the complete path to the image
        file2image(new_path_to_file)
        
        path2jpg =new_path_to_file.replace('.tiff', '.jpg')  
        pre_process_image(path2jpg)                                     #preprocessing the image 
        
        image2txt(new_folder_path + "/" + name_of_image[:-5] + "_gray_rotated_improved.jpg")
        print "OCR is finished successfully"    
        
        
    elif(filepath.endswith('.tif')):                                    #If the input file is a .tif file 
        new_folder_path = filepath[:-4] 
        os.makedirs(new_folder_path)                                    #make a new folder for the tif, name of the folder will be same as that of the tif
        shutil.move(filepath, new_folder_path)                          #tif is moved to the newly created of the same name 
        
        name_of_image = ""
    
        for w in reversed(filepath):                                    #to find the name of the image from the path 
            if(w == '/'):
                break
            else:
                 name_of_image= name_of_image + w                       #name_of_image stores the name of the image(reversed)
                
        name_of_image = name_of_image[::-1]                             #reversing the name of the image as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_image        #the complete path to the image 
        file2image(new_path_to_file)
        
        path2jpg =new_path_to_file.replace('.tif', '.jpg')
        pre_process_image(path2jpg)                                     #preprocessing the image 
        
        image2txt(new_folder_path + "/" + name_of_image[:-4] + "_gray_rotated_improved.jpg")
        print "OCR is finished successfully"    
        
    elif(filepath.endswith('.jpeg')):                                   #If the input file is a .jpeg file 
        new_folder_path = filepath[:-5] 
        os.makedirs(new_folder_path)                                    #make a new folder for the jpeg, name of the folder will be same as that of the jpeg
        shutil.move(filepath, new_folder_path)                          #jpeg is moved to the newly created of the same name 
        
        name_of_image = ""
    
        for w in reversed(filepath):                                    #to find the name of the image from the path 
            if(w == '/'):
                break
            else:
                 name_of_image= name_of_image + w                       #name_of_image stores the name of the image(reversed)
                
        name_of_image = name_of_image[::-1]                             #reversing the name of the image as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_image        #the complete path to the image
        file2image(new_path_to_file)
        
        path2jpg =new_path_to_file.replace('.png', '.jpg')   
        pre_process_image(path2jpg)                                     #preprocessing the image 
        
        image2txt(new_folder_path + "/" + name_of_image[:-5] + "_gray_rotated_improved.jpg")
        print "OCR is finished successfully"        
        
    elif(filepath.endswith('.png')):                                    #If the input file is a .png file 
        new_folder_path = filepath[:-4] 
        os.makedirs(new_folder_path)                                    #make a new folder for the png, name of the folder will be same as that of the png
        shutil.move(filepath, new_folder_path)                          #png is moved to the newly created of the same name 
        
        name_of_image = ""
    
        for w in reversed(filepath):                                    #to find the name of the image from the path 
            if(w == '/'):
                break
            else:
                 name_of_image= name_of_image + w                       #name_of_image stores the name of the image(reversed)
                
        name_of_image = name_of_image[::-1]                             #reversing the name of the image as it was originally reversed
     
        
        new_path_to_file = new_folder_path + "/" + name_of_image        #the complete path to the image 
         
        file2image(new_path_to_file)
        
        path2jpg =new_path_to_file.replace('.png', '.jpg')
        
        pre_process_image(path2jpg)                                     #preprocessing the image 
        
        image2txt(new_folder_path + "/" + name_of_image[:-4] + "_gray_rotated_improved.jpg")
        print "OCR is finished successfull" 
        
    elif(filepath.endswith('.doc')):
        new_folder_path = filepath[:-4] 
        os.makedirs(new_folder_path)                                    #make a new folder for the doc, name of the folder will be same as that of the doc
        shutil.move(filepath, new_folder_path)                          #doc is moved to the newly created of the same name 
        
        name_of_doc = ""
        for w in reversed(filepath):                                    #to find the name of the document from the path 
            if(w == '/'):
                break
            else:
                 name_of_doc = name_of_doc + w                          #name_of_doc stores the name of the image(reversed)
                
        name_of_doc = name_of_doc[::-1]                                 #reversing the name of the image as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_doc 
        temp = new_path_to_file[:-4]
        
        os.system('antiword ' + new_path_to_file + ' > ' + temp + '.txt')      #converting doc to txt 
        
    elif(filepath.endswith('.docx')):
        
        new_folder_path = filepath[:-5] 
        os.makedirs(new_folder_path)                                    #make a new folder for the docx, name of the folder will be same as that of the docx
        shutil.move(filepath, new_folder_path)                          #docx is moved to the newly created of the same name 
        
        name_of_docx = ""
    
        for w in reversed(filepath):                                    #to find the name of the document from the path 
            if(w == '/'):
                break
            else:
                 name_of_docx = name_of_docx + w                        #name_of_docx stores the name of the image(reversed)
                
        name_of_docx = name_of_docx[::-1]                               #reversing the name of the docx as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_docx         #the complete path to the docx
        
        newfile = open(new_path_to_file[:-5] + '.txt','w')
        document = opendocx(new_path_to_file)
        txt = getdocumenttext(document)
        
        for line in txt:
        	newfile.write(line.encode('ascii', 'ignore') + 'nn') 
        newfile.close()
        
    elif(filepath.endswith('.odt')):
        new_folder_path = filepath[:-4] 
        os.makedirs(new_folder_path)                                    #make a new folder for the odt, name of the folder will be same as that of the odt
        shutil.move(filepath, new_folder_path)                          #odt is moved to the newly created of the same name 
        
        name_of_odt = ""
        for w in reversed(filepath):                                    #to find the name of the document from the path 
            if(w == '/'):
                break
            else:
                 name_of_odt = name_of_odt + w                          #name_of_odt stores the name of the document(reversed)
                
        name_of_odt = name_of_odt[::-1]                                 #reversing the name of the odt as it was originally reversed
        new_path_to_file = new_folder_path + "/" + name_of_odt 
        
        
        os.system('odt2txt ' + new_path_to_file + ' > ' + new_path_to_file[:-4] + '.txt')
        
                
    
    
