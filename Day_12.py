# . Basic - Class and Object Creation

 # Problem: Create a Car class with attributes like brand, model, and year. Write a method that prints out the car’s information.

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def info(self):
        return self.brand,self.model,self.year

s1=Car("tata","range_rover",2025)
print(s1.info())