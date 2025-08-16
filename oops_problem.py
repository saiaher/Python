
# inheritance 
class vehicle:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
class car(vehicle):
    def __init__(self,model,brand,mailage):
        super().__init__(brand, model) 
        self.mailage=mailage 
    def info(self):
        return f"{self.model},{self.brand},{self.mailage}km/h"

s1=car("tata","punch",100)
print(s1.info())     

# Encapsulation
class account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount and amount<= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Invalid")

    def get_balance(self):
        return self.__balance


s1 = account("Alice", 10000)
s1.deposit(1000)
s1.withdraw(6000)
print("Current balance:", s1.get_balance())


# polymorphism

class cat:
    def speak(self):
        print("meow")
class dog:
    def speak(self):
        print("bark")
def animal_sound(animal):
    animal.speak()
s1=dog()
s2=cat()
animal_sound(s1)
animal_sound(s2)

# abstraction
from abc import ABC,abstractmethod
import math
class shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
class Rectingle(shape):
    def __init__(self,width,hight):
         self.width=width
         self.hight=hight

    def area(self):
        return self.width*self.width
    
class Cricle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

s1=Rectingle(5,10)
s2=Cricle(3)
print(s1.area())
print(s2.area())


    


    
    
        







