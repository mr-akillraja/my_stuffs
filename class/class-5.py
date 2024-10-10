#multiple inheritance example
class Parent1:
    def string1(self,str1):
        self.str1=str1

    def show_string1(self):
        print("the string1 is:",self.str1) 

class Parent2:
    def string2(self,str2):
        self.str2=str2

    def show_string2(self):
        print("the string2 is:",self.str2)

class Child(Parent1,Parent2):
    def string3(self,str3):
        self.str3=str3

    def show_string3(self):
        print("the string3 is:",self.str3)

    def final_strin(self):
        print(self.str1+self.str2+self.str3)    

c1=Child()
c1.string1("akill")
c1.string2("raja") 
c1.string3("M.R")
c1.show_string1()
c1.show_string2()
c1.show_string3()
c1.final_strin()                       