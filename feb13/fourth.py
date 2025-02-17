class Car:
    def __init__(self, brand, model = "Unknown"):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand is {self.brand}, Model is {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("BMW")

car1.display_info()
car2.display_info()