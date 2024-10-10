import fitz
import io
from PIL import Image

for i in range(211012001,211012010):
    doc=fitz.open(f"hallticket(am) - {i}.pdf")
    list_=doc.getPageImageList(0)
    for image_nums,image in enumerate(doc.getPageImageList(doc[0])):
        if image_nums%2!=0:
            xref=image[0]
            extract=doc.extractImage(xref)
            ext = extract["ext"]
            image_bytes = extract["image"]
            imgbytes=Image.open(io.BytesIO(image_bytes))
            imgbytes.save(open(f"image - {i}.{ext}", "wb"))
            