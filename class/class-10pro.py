class def1:
    def __init__(self):
        self.__a=10

    def m1(self):
        print("private")

v=def1()
v.m1()
print(v._def1__a)