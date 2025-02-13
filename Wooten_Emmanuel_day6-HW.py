'''Question 1: Design a Vehicle class with subclasses Car and Bike, each with unique attributes and behaviors.'''

#Answer 1:
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed  

    def show_info(self):
        return f"{self.brand} moving at {self.speed} mph."


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors  

    def honk(self):
        return "Car horn: Beep Beep!"


class Bike(Vehicle):
    def __init__(self, brand, speed, type_of_bike):
        super().__init__(brand, speed)
        self.type_of_bike = type_of_bike 

    def ring_bell(self):
        return "Bike bell: Ring Ring!"


my_car = Car("Toyota", 120, 4)
my_bike = Bike("Giant", 25, "Mountain")


print(my_car.show_info())  
print(my_car.honk())  

print(my_bike.show_info())  
print(my_bike.ring_bell())  


'''Question 2: Research and summarize why OOP is beneficial for large projects.'''
#Answer 2:

#OOP makes large projects easier to manage because: ✅ Encapsulation keeps related data and behaviors together, reducing complexity.
##- Inheritance allows code reuse, reducing duplication.
##- Polymorphism allows flexibility—one interface can work for different data types.
##- Modularity makes the codebase easier to debug and maintain by breaking it into objects.

#Example: Game Development (My favorite!)
#A game development company can define a Character class and create multiple game characters (Warrior, Mage, Archer) using inheritance and polymorphism. This avoids rewriting common features (like movement or health).



'''
Question 3: Define a BankAccount class with attributes balance and methods deposit and withdraw.
Create a subclass SavingsAccount with an additional method add_interest.
'''

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount}. New Balance: ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew: ${amount}. New Balance: ${self.balance}"
        return "Insufficient funds!"


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate 

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added: ${interest}. New Balance: ${self.balance}"


savings = SavingsAccount(1000)  


print(savings.deposit(500))  
print(savings.add_interest())  
print(savings.withdraw(2000))  
