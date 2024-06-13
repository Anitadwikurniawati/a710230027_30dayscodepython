class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year) 
        self.doors = doors

    def car_info(self):
        return f"{self.vehicle_info()} with {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year) 
        self.has_sidecar = has_sidecar

    def motorcycle_info(self):
        sidecar = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{self.vehicle_info()} {sidecar}"

car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, False)

print(car.car_info())  
print(motorcycle.motorcycle_info())  