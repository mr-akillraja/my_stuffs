#METHOD OVERRIDING
class test:
    def dec1(self):
        print("akill is riding.")
    
class west(test):
    def dec1(self):
        print("akill is overrriding")

v=west()
v.dec1()