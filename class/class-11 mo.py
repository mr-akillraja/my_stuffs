class version1:
    def dec1(self):
        print("version 1")
                              #parent child relationship
class version2(version1):
    def dec2(self):
        print("version2")

c=version2()
c.dec1()
c.dec1()