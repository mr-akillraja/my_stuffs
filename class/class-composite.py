class component:
    def __init__(self):
        print("component class created")

    def m1(self):
        print("component class m1 executed.")

class composite(component):
    def __init__(self):
        print("composite class obj created ")
    
    def m2(self):
        print("component class m2 executed.")
        
       

obj2=composite()
obj2.m2()
