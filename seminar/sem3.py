import math


# ---------- Classes ----------

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"{self.name} {self.family}, nationality: {self.nationality}")


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        super().print()
        print(f"  Student at {self.university}, year {self.yearofstudy}")


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        super().print()
        print(f"  Lecturer at {self.university}, experience: {self.experience} years")


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print(self):
        print(f"{self.name} - {self.position}, salary: {self.salary:.2f}")


class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def print(self):
        super().print()
        print(f"  Department: {self.department}")


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print(f"{self.brand} {self.model} ({self.year})")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def print(self):
        super().print()
        print(f"  Doors: {self.doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def print(self):
        super().print()
        print(f"  Engine capacity: {self.engine_capacity} cc")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} ({self.age} y.) says: Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} ({self.age} y.) says: Meow!")


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print(self):
        print(f'"{self.title}" by {self.author}, {self.year}')


class EBook(Book):
    def __init__(self, title, author, year, format, size):
        super().__init__(title, author, year)
        self.format = format
        self.size = size

    def print(self):
        super().print()
        print(f"  Format: {self.format}, size: {self.size} MB")


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds to withdraw {amount:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}")

    def print(self):
        print(f"Account owner: {self.owner}, balance: {self.balance:.2f}")


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # annual rate in percent

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest:.2f}")

    def print(self):
        super().print()
        print(f"  Annual interest rate: {self.interest_rate}%")


# ---------- Tasks ----------

def task_1():
    people = [
        Person("Ivan", "Petrov", 30, "Bulgarian"),
        Person("Anna", "Schmidt", 25, "German"),
        Person("Marco", "Rossi", 41, "Italian"),
    ]
    for p in people:
        p.print()


def task_2():
    students = [
        Student("Maria", "Ivanova", 20, "Bulgarian", "TU-Sofia", 2),
        Student("John", "Smith", 22, "British", "Oxford", 4),
    ]
    for s in students:
        s.print()


def task_3():
    lecturers = [
        Lecturer("Georgi", "Dimitrov", 50, "Bulgarian", "TU-Sofia", 22),
        Lecturer("Claire", "Dubois", 38, "French", "Sorbonne", 10),
    ]
    for l in lecturers:
        l.print()


def task_4():
    employees = [
        Employee("Petar", "Developer", 4500),
        Employee("Elena", "Designer", 3800),
        Employee("Nikolay", "Tester", 3200),
    ]
    for e in employees:
        e.print()


def task_5():
    managers = [
        Manager("Daniela", "Manager", 6500, "IT"),
        Manager("Stoyan", "Manager", 6000, "Sales"),
    ]
    for m in managers:
        m.print()


def task_6():
    vehicles = [
        Vehicle("Toyota", "Corolla", 2018),
        Vehicle("Volvo", "FH16", 2021),
        Vehicle("Ford", "Transit", 2015),
    ]
    for v in vehicles:
        v.print()


def task_7():
    cars = [
        Car("BMW", "320d", 2019, 4),
        Car("Mini", "Cooper", 2020, 2),
    ]
    for c in cars:
        c.print()


def task_8():
    motorcycles = [
        Motorcycle("Honda", "CBR600RR", 2017, 599),
        Motorcycle("Yamaha", "MT-07", 2022, 689),
    ]
    for m in motorcycles:
        m.print()


def task_9():
    animals = [Dog("Rex", 5), Cat("Tom", 3), Animal("Generic", 1)]
    for a in animals:
        a.sound()


def task_10():
    books = [
        Book("Pod igoto", "Ivan Vazov", 1894),
        Book("1984", "George Orwell", 1949),
        Book("The Hobbit", "J. R. R. Tolkien", 1937),
    ]
    for b in books:
        b.print()


def task_11():
    ebooks = [
        EBook("Clean Code", "Robert C. Martin", 2008, "PDF", 4.5),
        EBook("Fluent Python", "Luciano Ramalho", 2015, "EPUB", 12.3),
    ]
    for e in ebooks:
        e.print()


def task_12():
    shapes = [Rectangle(3, 4), Circle(2), Rectangle(5, 1.5), Circle(1)]
    for s in shapes:
        print(f"{type(s).__name__}: area = {s.area():.2f}")


def task_13():
    acc = Account("Ivan Petrov", 100)
    acc.print()
    acc.deposit(250)
    acc.withdraw(80)
    acc.withdraw(1000)
    acc.print()


def task_14():
    acc = SavingsAccount("Maria Ivanova", 1000, 5)
    acc.print()
    acc.deposit(500)
    acc.add_interest()
    acc.withdraw(200)
    acc.print()


def task_15():
    people = [
        Person("Ivan", "Petrov", 30, "Bulgarian"),
        Student("Maria", "Ivanova", 20, "Bulgarian", "TU-Sofia", 2),
        Lecturer("Georgi", "Dimitrov", 50, "Bulgarian", "TU-Sofia", 22),
    ]
    for p in people:
        print(f"[{type(p).__name__}]")
        p.print()


# ---------- Menu ----------

TASKS = {
    1: task_1, 2: task_2, 3: task_3, 4: task_4, 5: task_5,
    6: task_6, 7: task_7, 8: task_8, 9: task_9, 10: task_10,
    11: task_11, 12: task_12, 13: task_13, 14: task_14,
    15: task_15,
}

if __name__ == "__main__":
    while True:
        choice = input("\nChoose a task (1-15) or 0 to exit: ")
        if choice == "0":
            break
        if choice.isdigit() and int(choice) in TASKS:
            TASKS[int(choice)]()
        else:
            print("Invalid choice.")
