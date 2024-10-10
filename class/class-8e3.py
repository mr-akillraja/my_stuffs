class Emp:
    def setname(self,n):
        self.__name=n

    def getname(self):
        return self.__name

    def setmarks(self,m):
        self.__marks=m

    def getname(self):
        return self.__marks

    def dis(self):
        print("name:",self.__name) 
        print("marks:",self.__marks) 

s=Emp()
s.setname("akill raja")
s.setmarks(90.6)
s.dis()