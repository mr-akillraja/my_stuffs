class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def  __add__(self,r):
        return self.a+r.a,self.b+r.b

o=Test(10,'65')
op=Test(5,"akill")

print(o+op)


#comparsion operator
class t:
    def __init__(self,a):
        self.a=a

    def __gt__(self,o):
        if(self.a>o.a):
            return True
        else:
            False

o1=t(5)
o2=t(6)
if(o1>o2):
    print("object1 is greater than object2")
else:
    print("object2 is greater than object1")    