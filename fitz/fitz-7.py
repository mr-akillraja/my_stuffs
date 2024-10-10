import fitz
import io
from PIL import Image


def imgextraction():
    doc=fitz.open('002.pdf')
    list_=doc.getPageImageList(0)
    length_image=len(list_)
    print(list_)
#extracting the images whiich is in odd position in the pdf
    for image_nums,image in enumerate(doc.getPageImageList(doc[0])):
        if image_nums%2!=0:
            xref=image[0]
   
#method returns all the information about the image, including its byte code and image extension
            extract=doc.extractImage(xref)
#getting the extension of the image 
            ext = extract["ext"]
#accesing the image itself    
            image_bytes = extract["image"]
#getting the result in bytes and trying to load the image    
            imgbytes=Image.open(io.BytesIO(image_bytes))
#saving the image with the extension    
            imgbytes.save(open(f"image - {image_nums}.{ext}", "wb"))

    print(f'total images present in the pdf of the current page {length_image}')    


imgextraction()
