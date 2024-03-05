class Dog:
    def __init__(self, name, age, colour):  # method called whenever we create a new dog instance
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        print(f"{self.name} is a {self.age} year old {self.colour} dog.")

    def change_age(self, age):
        self.age = age


# Creating Spot object as an instance of Dog class
dog1 = Dog("Spot", 13, "brown")
dog2 = Dog("Jazz", 47, "white")
dog3 = Dog("Jefferson", 20, "blue")

Dog.print_details(dog1)
Dog.print_details(dog2)
Dog.print_details(dog3)

dog1.change_age(17)
dog2.change_age(4.7)
dog3.change_age(2)

print()
Dog.print_details(dog1)
Dog.print_details(dog2)
Dog.print_details(dog3)