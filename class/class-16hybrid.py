class cals:
    def num(self):
        self.a=int(input("enter the number1 "))
        self.b=int(input("enter the number2 "))

class addition(cals):
    def add(self):
        self.num()
        c=self.a+self.b
        print("addition : ",c)

class subtraction(cals):
    def sub(self):
        self.num()
        c=self.a-self.b
        print("subtraction : ",c)

class arthimethic(addition,subtraction):
    def arth(self):
        self.add()
        self.sub()

ob=arthimethic()
ob.arth()        
