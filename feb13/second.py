class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Corolla")

print(f"Brand is {car.brand}, Model is {car.model}")