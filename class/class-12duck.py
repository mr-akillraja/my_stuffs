class duck:
    def sound(self):
        print("quak quack!")

class dog:
    def sound(self):
        print("woof woof!")

class cat:
    def sound(self):
        print("meow meow!")

def all_sound(ak):
    ak.sound()

c=dog()
all_sound(c)