class Bus:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        print(f"Bus {self.number} is on route {self.route} and is driven by {self.driver}")


# Initialise the buses
b1 = Bus(2394, "Orbiter", "George")
b2 = Bus(9826, "Green", "Brittany")
b3 = Bus(1223, "Yellow", "Dave")
