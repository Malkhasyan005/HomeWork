class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand is {self.brand}, Model is {self.model}")

car = Car("Toyota", "Corolla")
car.display_info()