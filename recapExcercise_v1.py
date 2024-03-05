class Staff:
    def __init__(self, name, age, id, dob, job):
        self.name = name
        self.age = age
        self.id = id
        self.dob = dob
        self.job = job

    def show(self):
        print(f"My name is {self.name}, and I am {self.age} years old. My ID is {self.id}, and I was born on "
              f"{self.dob}. My Job title is '{self.job}.'")


class Management(Staff):
    def __init__(self, name, age, id, dob, job, car):
        super().__init__(name, age, id, dob, job)
        self.car = car

    def car_display(self):
        print(f"My company car is a {self.car}.")


class Clerical(Staff):
    def __init__(self, name, age, id, dob, job, typing):
        super().__init__(name, age, id, dob, job)
        self.typing = typing

    def typing_display(self):
        print(f"My typing speed is {self.typing} words per minute.")


class Factory(Staff):
    pass


# Main...
m1 = Management("Timothy", 22, 42891, "27/02/98", "CFO", "Lamborghini")
m1.show()
m1.car_display()
print()
m2 = Management("Joel", 41, 92956, "03/05/99", "CEO", "Ford F-150")
m2.show()
m2.car_display()
print()
c1 = Clerical("Sarah", 33, 74962, "12/03/02", "Market Researcher", 132)
c1.show()
c1.typing_display()
print()
c2 = Clerical("Bobby", 51, 20948, "14/12/05", "Finance Manager", 129)
c2.show()
c2.typing_display()
print()
f1 = Factory("Gerald", 29, 44638, "21/9/87", "Forklift Operator")
f1.show()
print()
f2 = Factory("Yorkshire", 38, 28476, "28/11/02", "Floor Worker")
f2.show()
print()
