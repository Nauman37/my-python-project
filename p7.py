class animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(animal):
    def bark(self):
        print("Woof")

my_dog=Dog()
my_dog.speak()
my_dog.bark()