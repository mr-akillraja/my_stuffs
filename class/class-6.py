class Parent:
    def name(self,name):
        self.name=name

    def show_name(self):
        print("the name is:",self.name)
       
class Child:
    def Age(self,age):
        self.age=age

    def show_age(self):
        print("the age is:",self.age) 

class Grandchild(Parent,Child):
    def Gender(self,gender):
        self.gender=gender

    def show_gender(self):
        print("the gender is",self.gender)

c=Grandchild()
c.name("akill")
c.Age(19)
c.Gender("male")
c.show_name()
c.show_age()
c.show_gender()            