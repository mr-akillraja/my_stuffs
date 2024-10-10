#getting the links which is presented inside the pdf

import fitz 

doc=fitz.open('aks.pdf')
page=doc[0]
link_s=page.get_links()
print(link_s)


#checking the links all the pages which are presented
for i in doc:
    links=i.get_links()
print(links)