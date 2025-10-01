# Learn:

# Classes, objects

# Attributes, methods

# Constructors (__init__)

# Inheritance & polymorphism

# Magic methods (__str__)

# Challenges (Day 6):

# Create Car class with brand, speed.
from re import A


class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
# Add methods to accelerate, brake.
    def accelerate(self, increment):
        self.speed += increment
    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)

# Create BankAccount with deposit & withdraw.
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        # self.balance = self.balance - amount if amount <= self.balance else self.balance = 0
        # self.balance = max(0, self.balance - amount)
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Inherit SavingAccount from BankAccount.
class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

# Create Animal => inherit Dog, Cat.
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create Rectangle class with area & perimeter.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create Student class => store marks, calc average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
# Override __str__ to display object nicely.
    def __str__(self):
        return f"Student {self.name}, Average: {self.average():.2f}"

# Create ShoppingCart class with add/remove item.
class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items else []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not in cart")
    def __str__(self):
        return f"ShoppingCart with items: {', '.join(self.items)}"

# Create Library system with books issue/return.
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, title, author):
        self.books[title] = {'author': author, 'available': True}

    def issue_book(self, title):
        if title in self.books and self.books[title]['available']:
            self.books[title]['available'] = False
            print(f"Issued book: {title}")
        else:
            print("Book not available")

    def return_book(self, title):
        if title in self.books and not self.books[title]['available']:
            self.books[title]['available'] = True
            print(f"Returned book: {title}")

    def __str__(self):
        return f"Library with books: {','.join(self.books)}"

def main():
    # Car
    car = Car("Honda")
    car.accelerate(50)
    car.brake(20)
    print(car.speed)  # 30

    # BankAccount => Saving Account
    acc = SavingAccount("Alice", 1000)
    acc.apply_interest()
    print(acc.balance)  # 1020.0

    # Animal => Dog, Cat
    animals = [Dog(), Cat()]
    for a in animals:
        print(a.speak())  # Woof! Meow!

    # Rectangle
    rect = Rectangle(4, 5)
    print(rect.area())      # 20
    print(rect.perimeter()) # 18

    # Student
    s = Student("Bob", [80, 90, 70])
    print(s)  # Student Bob, Average: 80.00

    # ShoppingCart
    cart = ShoppingCart()
    cart.add_item("Apple")
    cart.add_item("Milk")
    print(cart)  # Cart: Milk
    cart.remove_item("Apple")
    print(cart)  # Cart: Milk

    # Library
    lib = Library()
    lib.add_book("1984", "George Orwell")
    # books = {"1984": {"author": "George Orwell", "status": "available"}}
    lib.issue_book("1984")
    # "1984" => status becomes "issued"
    # books = {"1984": {"author": "George Orwell", "status": "issued"}}
    lib.add_book("To Kill a Mockingbird", "Harper Lee")
    # books = {
    #   "1984": {"author": "George Orwell", "status": "issued"},
    #   "To Kill a Mockingbird": {"author": "Harper Lee", "status": "available"}
    # }
    lib.issue_book("1984")  # # Already issued => prints: "Book not available"
    lib.issue_book("To Kill a Mockingbird") # status = "issued"
    lib.issue_book("To Kill a Mockingbird") # # Already issued => prints: "Book not available"
    print(lib)  # Library with books: 1984
    lib.return_book("1984")
    # "1984" status back => "available"
    # books = {
    #   "1984": {"author": "George Orwell", "status": "available"},
    #   "To Kill a Mockingbird": {"author": "Harper Lee", "status": "issued"}
    # }
    print(lib)  # Library with books: 1984
    lib.issue_book("1984")


if __name__ == "__main__":
    main()
