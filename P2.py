class Car:
    def __init__(self,brand,model,year,color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color

    def paint_car(self,new_color):
        old_color=self.color
        self.color=new_color
        print(f"i changed my cars color from {old_color} to {self.color}")

    def describe(self):
        print(f"This is my {self.color} {self.brand} {self.model} from {self.year}")
    
    def newer_car(self,other_car):
        if self.year > other_car.year:
            print(f"The {self.brand} {self.model} from {self.year} is newer than {other_car.brand} {other_car.model} from {other_car.year}")
        elif self.year < other_car.year:
            print(f" apparently the {other_car.brand} {other_car.model} from {other_car.year} is newer from {self.brand} {self.model} from {self.year}")
        if self.year == other_car.year:
            print("Both the cars are the same year :)")

car1=Car("toyota", "camry", 2040, "blue")
car2=Car("maruti", "Zx10r", 2035, "neon")

car1.paint_car("viodigo")
