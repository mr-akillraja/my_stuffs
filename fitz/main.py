import fitz
import io
from PIL import Image
import requests



headers={
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }

#extracting the images from the downloaded pdf            
def image_extraction():   
    doc=fitz.open(f"hallticket(ds)- {i}.pdf")
    list_=doc.getPageImageList(0)
    image = list_[1]
    xref=image[0]
    extract=doc.extractImage(xref)
    ext = extract["ext"]
    image_bytes = extract["image"]
    imgbytes=Image.open(io.BytesIO(image_bytes))
    imgbytes.save(open(f"image - {i}.{ext}", "wb"))  


#downloading the hall tickets from the website 
for i in range(2036010001,2036010045):
    try:
        r=requests.get(f"https://coe.annamalaiuniversity.ac.in/reg_hall_qr_print1.php?rollno={i}&exam=ENGG",headers=headers)
        print(r)
        with open(f"hallticket(ds)- {i}.pdf",'wb') as f:
            f.write(r.content)
            image_extraction()
    except:
        pass        

       
    

