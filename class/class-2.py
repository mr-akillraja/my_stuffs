class Phone:
    def set_color(self,color):
        self.color=color
        
    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        print( self.color)

    def show_cost(self):
        print(self.cost)

    def play_game(self):
        print("playing game")    

p1=Phone()
p1.set_color('green')
p1.show_color()
p1.set_cost(500)
p1.set_color("blue")
p1.show_color()

p1.show_cost()        
p1.play_game()