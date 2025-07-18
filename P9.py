class vehicle:
    def __init__(self,brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
    
    def intro(self):
        print(f"This is {self.color} {self.brand} {self.model} from {self.year} ")
    
    def leaks(self):
        print(f"He has a {self.brand} {self.model} from {self.year}")

class car(vehicle):
    def __init__(self,brand,model,year,old_color,new_color):
        super().__init__(brand, model, year,old_color)
        self.color=new_color
        print(f"Before:{old_color} red The new color of the car now is {self.color}")

    def show_color(self):
        print(f"The car color is {self.color}")

my_car=car("toyota","Camry",2003,"red","blue")
my_car.show_color()