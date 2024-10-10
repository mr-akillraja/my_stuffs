class bank:
   

    def ram(self):
        print("the name:ram")
        print("the account number is:1234532")
        print("salary is:2000")
        print("\n")

    def __init__(self):
        self.__value=10    

    def sam(self):
        #print("the value is",self._value)
        print("the name:sam")
        print("the account number is:145332")
        print("salary is:450900")    

    


c=bank()
c.ram()
c.sam()
print("the value is",c._bank__value)#calling the private data using class
#print("the value is:",c._value)