import fitz 

#getting the pages as one  image
doc=fitz.open('002.pdf')
page=doc[0]
pix=page.get_pixmap()
pix.save("page-.png" )


#getting the all pages as images of the pdf

for i in doc:
    pixes=i.get_pixmap()
    pixes.save(f'ampages{i}.png') 