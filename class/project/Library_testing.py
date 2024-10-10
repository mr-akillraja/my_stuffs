class Library:
    def book(self,book):
        self.book_list=['akill','fap','edwin','shalu']

   
    def add(self):
        self.user=input("enter the bookname to add: ")
        self.book_list.append(self.user)
        print("the book has been added>>>>>>",self.user)
        print(self.book_list)

    def lend(self):
        print("select a book from the list",self.book_list)
        choose=input("choose a book you want!")
        if choose in self.book_list:
            ind=self.book_list.index(choose)
            self.book_list.pop(ind)
            print("the choosed book is",choose)
            print("showing the remaining books",self.book_list)
        else:
            print("book not found!!!!")    
        

    def return_book(self):
        choose=input("enter the book name :")
        ind=self.book_list.index(choose)
        self.book_list.append(ind)
        print("the book has returned and added to library",self.book_list)

    
    def display(self):
        book=self.book_list
        for i in list(book):
          print(i)

class dis(Library):
    def disp(self):
        print("1.Add The Book.")
        print("2.Lending a Book U Need.")
        print("3.Returning The Book.")
        print("4.Display The Books You Have!!")
        user=input("enter the choice :")
        if user==1:
            return self.add()
        elif user==2:
             return self.lend()
        elif user==3:
            return self.return_book()
        elif user==4:
            return self.display()
        else:
            print("enter a VALID OPTION!!!!!!!")      





obj=dis()
obj.disp()
