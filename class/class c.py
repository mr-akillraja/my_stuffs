class Cals:
    def __init__(self,a,b):
        self.a=int(input("enter the value1 :"))
        self.b=int(input("enter the value2 :"))

    def add(self):
        c=self.a+self.b
        print("ADDITION:",c) 

    def sub(self):
        c=self.b-self.a
        print("SUBTRACTION:",c)

    def multi(self):
        c=self.a*self.b
        print("MULTIPLICATION:",c)      

    def divi(self):
        c=self.a/self.b
        print("DIVISION:",c) 

c=Cals(12,45)
c.add()
c.sub()
c.multi()
c.divi()
