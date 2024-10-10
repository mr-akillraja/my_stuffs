#extracting the text from the pdf

import fitz 

#getting the text of the corresponding page in pdf
doc=fitz.open('aks.pdf')
page=doc[0]
text1=page.get_text()
with open('text.txt','wb') as f:
#converting the string to bytes using encode    
    f.write(text1.encode('UTF-8'))




## for getting the all the text in pdf
for i in doc:
    texts=i.get_text()
    with open(f'text from pdf pgno{i}.txt','wb') as f:
        f.write(texts.encode('UTF-8'))