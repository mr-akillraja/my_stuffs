from abc import ABC,abstractmethod
class colleges:
    def types(self):
        pass

class Mcolleges():
    def types(self):
        print("i am a medical student")

class Ecollege():
    def types(self):
        print("i am a engineering a student")

    def dept(self,c):
        self.couse=c

    def deptdis(self):
        print("the current dept is:",self.couse)        

class Acollege():
    def ty(self):
        print("i am a arts and science student")


m=Mcolleges()
m.types()
e=Ecollege()
e.types()
e.dept("cse")
e.deptdis()
a=Acollege()
a.ty()
