#extracting the annots from the pdf

import fitz 

doc=fitz.open('aks.pdf')
page=doc[0]
link_s=page.annots()
print(link_s)

#multiple annots
for i in doc:
    annots=i.annots()
    print(annots)

#annots
#A file with the ANNOT file extension is an Adobe Digital Editions Annotations file. 
# It's saved in the XML format and used to store auxiliary data for EPUB files like notes, 
# bookmarks, highlights, and other sorts of "meta" data.