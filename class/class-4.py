#using super function
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def vehicle_details(self):
        print("i'm a vehicle")
        print("the mileage of the vehicle is",self.mileage)
        print("the cost of the car is",self.cost)    


class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp

    def show_car_deatils(self):
        print("it's a car")
        print("no of tyres is",self.tyres)
        print("the hp is",self.hp)


c1=Car(4000000,4,300,23)
c1.vehicle_details()
c1.show_car_deatils()

