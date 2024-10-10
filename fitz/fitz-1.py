#access of pages of a pdf
import fitz 

doc=fitz.open('aks.pdf')
page = doc.load_page(0)  
print(page)

#another type of page loading  

page1=doc[0]
print(page1)

#getting total pages:
for i in doc:
    print(i)
 