class Enemy:
    def size(self,size):
        self.size=size

    def position(self,position):
        self.position=position

    def move(self,move):
        self.move=move

    def dead(self,dead):
        self.dead=dead


class Enemys(Enemy):
    def enemy1(self):
        print("the size of the enemy is:",self.size)
        print("the postion of the enemy1 is:",self.position)
        print("the move of the enemy1 is:",self.move)
        print("the dead will be:",self.move)

    def enemy2(self):
        print("the size of the enemy2 is:",self.size)
        print("the postion of the enemy2 is:",self.position)
        print("the move of the enemy2 is:",self.move)
        print("the dead will be:",self.move)

    def enemy3(self):
        print("the size of the enemy3 is:",self.size)
        print("the postion of the enemy3 is:",self.position)
        print("the move of the enemy3 is:",self.move)
        print("the dead will be:",self.move)    


e=Enemys()
e.size(10)
e.position("right")
e.move('upwards')
e.dead("touching the mushroom")
e.enemy3() 
e.enemy2()       