# import array as arr
# a=arr.array('s',['a','b','c','d','e','f'])
# for i in range(len(a)):
#     print("Element at index",end="")
#     print("%d is %d"%(i,a[i]))


# import array as arr

# a = arr.array('str', ['adi', 'bol', 'cou', 'dfd', 'egf', 'fbv'])

# for i in range(len(a)):
#     print("Element at index", end=" ")
#     print("%d is %s" % (i, a[i]))



#<==================================16/01/2024==================================>


# class Product:
#     def __init__(self, id , name, price):
#         # print("Constructor Called")
#         self.id = id
#         self.name = name
#         self.price = price

#     def display_product(self):
#         print(self.id , self.name , self.price)

# class Car:
#     pass


# p1 = Product(101 , "Remote" , 200)
# p2 = Product(102 , "Keyboard" , 500)


# print(isinstance(p1,Product))
# print(isinstance(p1,Car))


# p1.display_product()
# p2.display_product()


# class grandparent:
#     def init(self,gname):
#         print("Grandparents")
#         self.gname=gname
# class parents(grandparent):
#     def init(self,pname):
#         print("Parents")
#         self.pname=pname
#         super().init(gname)
# class child(parents):
#     def init(self,cname):
#         print("Child")
#         self.cname=cname
#         super().init(pname,gname)


# class father:
#     def init(self,fname):
#         print("Father")
#         self.fname=fname
# class mother:
#     def init(self,mname):
#         print("Mother")
#         self.mname=mname

# class child1(father,mother):
#     def init(self,name,fname,mname):
#         print("child1 class")
#         self.name=name
#         father.init(self,fname)
#         mother.init(self,mname)
#     def display(self):
#         print(f"{self.name} parents name are {self.fname} and {self.mname}")



# Assignment 1 

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # Example usage:
# rectangle = Rectangle(5, 3)
# print("Area:", rectangle.area())
# print("Perimeter:", rectangle.perimeter())


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Grade:", self.grade)

# # Example usage:
# student1 = Student("Alice", 17, "A")
# student2 = Student("Bob", 16, "B")

# print("Student 1 details:")
# student1.display_details()

# print("\nStudent 2 details:")
# student2.display_details()


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Grade:", self.grade)

#     def calculate_grade(self, percentage):
#         if percentage >= 90:
#             return "A"
#         elif percentage >= 80:
#             return "B"
#         elif percentage >= 70:
#             return "C"
#         elif percentage >= 60:
#             return "D"
#         else:
#             return "F"

# # Example usage:
# student1 = Student("Alice", 17, "A")
# student2 = Student("Bob", 16, "B")

# print("Student 1 details:")
# student1.display_details()
# percentage1 = 85
# print("Grade for {}%: {}".format(percentage1, student1.calculate_grade(percentage1)))

# print("\nStudent 2 details:")
# student2.display_details()
# percentage2 = 75
# print("Grade for {}%: {}".format(percentage2, student2.calculate_grade(percentage2)))


# class Animal:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age

#     def display_info(self):
#         print("Name:", self.name)
#         print("Species:", self.species)
#         print("Age:", self.age)

# class Lion(Animal):
#     def roar(self):
#         print("Roar!")

# class Elephant(Animal):
#     def trumpet(self):
#         print("Trumpet sound!")

# class Giraffe(Animal):
#     def neck_length(self):
#         print("Neck length:", "Long")  # Assuming all giraffes have long necks

# # Example usage:
# lion = Lion("Simba", "Lion", 5)
# elephant = Elephant("Dumbo", "Elephant", 10)
# giraffe = Giraffe("Melman", "Giraffe", 7)

# print("Lion details:")
# lion.display_info()
# lion.roar()

# print("\nElephant details:")
# elephant.display_info()
# elephant.trumpet()

# print("\nGiraffe details:")
# giraffe.display_info()
# giraffe.neck_length()


# class Bank:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposit of ${} successful.".format(amount))
#         else:
#             print("Invalid amount for deposit.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal of ${} successful.".format(amount))
#         else:
#             print("Insufficient funds or invalid amount for withdrawal.")

#     def display_balance(self):
#         print("Account Holder:", self.account_holder)
#         print("Balance: ${}".format(self.balance))

# # Example usage:
# account1 = Bank("Alice", 1000)
# account2 = Bank("Bob", 500)

# account1.display_balance()
# account1.deposit(200)
# account1.display_balance()
# account1.withdraw(300)
# account1.display_balance()

# print("\n")

# account2.display_balance()
# account2.deposit(100)
# account2.display_balance()
# account2.withdraw(700)
# account2.display_balance()


# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year

#     def display_details(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Publication Year:", self.publication_year)


# class EBook(Book):
#     def __init__(self, title, author, publication_year, file_size):
#         super().__init__(title, author, publication_year)
#         self.file_size = file_size

#     def display_details(self):
#         super().display_details()
#         print("File Size:", self.file_size)


# # Example usage:
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# book1.display_details()

# print("\n")

# ebook1 = EBook("1984", "George Orwell", 1949, "1.2 MB")
# ebook1.display_details()


# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def calculate_area(self):
#         return self.side ** 2

# # Example usage:
# circle = Circle(5)
# print("Area of circle:", circle.calculate_area())

# square = Square(4)
# print("Area of square:", square.calculate_area())


# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def is_adult(self):
#         return self.age >= 18

# # Example usage:
# person1 = Person("Alice", 25, "123 Main St")
# print(person1.name, "is an adult?", person1.is_adult())

# person2 = Person("Bob", 15, "456 Elm St")
# print(person2.name, "is an adult?", person2.is_adult())


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def is_old(self):
#         current_year = 2024  # Assuming the current year is 2024
#         return current_year - self.year > 10

# # Example usage:
# car1 = Car("Toyota", "Camry", 2010)
# print("Is car1 old?", car1.is_old())  # Output will depend on the current year

# car2 = Car("Honda", "Accord", 2018)
# print("Is car2 old?", car2.is_old())  # Output will depend on the current year


# class BankAccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposit of ${} successful.".format(amount))
#         else:
#             print("Invalid amount for deposit.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal of ${} successful.".format(amount))
#         else:
#             print("Insufficient funds or invalid amount for withdrawal.")

#     def display_balance(self):
#         print("Account Holder:", self.account_holder)
#         print("Account Number:", self.account_number)
#         print("Balance: ${}".format(self.balance))


# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, account_holder, balance, interest_rate):
#         super().__init__(account_number, account_holder, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         print("Interest earned: ${}".format(interest))
#         return interest


# # Example usage:
# savings_account = SavingsAccount("123456789", "Alice", 1000, 5)

# savings_account.display_balance()
# savings_account.deposit(200)
# savings_account.display_balance()
# savings_account.withdraw(300)
# savings_account.display_balance()

# savings_account.calculate_interest()

#======================================================================================================================================================================

#Assignmnt 2

# import math

# class Shape:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Example usage:
# rectangle = Rectangle(5, 3)
# print("Rectangle Area:", rectangle.area())
# print("Rectangle Perimeter:", rectangle.perimeter())

# circle = Circle(4)
# print("\nCircle Area:", circle.area())
# print("Circle Circumference:", circle.perimeter())


# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

# class Bird(Animal):
#     def make_sound(self):
#         return "Chirp!"

# # Example usage demonstrating polymorphism:
# animals = [Dog(), Cat(), Bird()]

# for animal in animals:
#     print(animal.__class__.__name__ + " says:", animal.make_sound())



# class Engine:
#     def start(self):
#         print("Engine started")


# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Composition: Car has an Engine

#     def start(self):
#         self.engine.start()

# # Example usage:
# my_car = Car()
# my_car.start()  # This will call the start method of the Engine object within the Car


# class Person:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary

#     def set_name(self, name):
#         self.__name = name

#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Age cannot be negative.")

#     def set_salary(self, salary):
#         if salary >= 0:
#             self.__salary = salary
#         else:
#             print("Salary cannot be negative.")

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age

#     def get_salary(self):
#         return self.__salary


# # Example usage:
# person = Person("Alice", 30, 50000)

# print("Name:", person.get_name())
# print("Age:", person.get_age())
# print("Salary:", person.get_salary())

# person.set_age(-5)  # Attempting to set negative age
# person.set_salary(-1000)  # Attempting to set negative salary

# print("\nAfter attempting to set negative values:")
# print("Name:", person.get_name())
# print("Age:", person.get_age())  # Age should remain unchanged
# print("Salary:", person.get_salary())  # Salary should remain unchanged


# class A:
#     def display_a(self):
#         print("Method display_a from class A")

# class B:
#     def display_b(self):
#         print("Method display_b from class B")

# class C:
#     def display_c(self):
#         print("Method display_c from class C")

# class D(A, B):
#     pass

# class E(D, C):
#     pass

# # Example usage:
# obj_e = E()
# obj_e.display_a()  # Call method from class A
# obj_e.display_b()  # Call method from class B
# obj_e.display_c()  # Call method from class C

# import tkinter as tk
# from tkinter import *

# m = tk.Tk()

# button = Button(m, text="Submit", width=25, bg='blue', activebackground='yellow')  
# button.pack()

# root = Tk()

# frame = Frame(root)
# frame.pack()


# buttonframe = Frame(root)
# bottomframe.pack(side = BOTTOM)

# redbutton = Button(frame , text = "red" , fg = 'red')


# m.mainloop()


# from tkinter import *

# top = Tk()
# mb = Menubutton ( top, text = &amp;quot;GfG&amp;quot;)
# mb.grid()
# mb.menu = Menu ( mb, tearoff = 0 )
# # mb[&amp;quot;menu&amp;quot;] = mb.menu
# cVar = IntVar()
# aVar = IntVar()
# mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
# mb.menu.add_checkbutton ( label = 'About', variable = aVar )
# mb.pack()
# top.mainloop()


# from tkinter import *
# main = Tk()
# ourMessage ='This is our Message'
# messageVar = Message(main, text = ourMessage)
# messageVar.config(bg='lightgreen')
# messageVar.pack( )
# main.mainloop( )


# # Label Basic
# import tkinter as tk

# lb = tk.Label(None, text='Hello World')
# lb.pack()

# tk.mainloop()


# create 2 classes employee and define a method get salary that returns the salary of "50000" 
# create a class student and define a method grt salaray that return "am still learning"
# create a method get_status(obj) and print(obj.get_status())
# obj = employee()
# get_status(obj)


# class Employee:
#     def get_salary(self):
#         return 50000
#     def get_dep(self):
#         return "AIML"

class Student:
    def get_salary(self):
        return "am still learning"
    
# class Different:
#     pass

# def get_status(obj):
#     if isinstance(obj, Employee):
#         print("The salary is: ", obj.get_salary())
#         print("The department is: ", obj.get_dep())
#     elif isinstance(obj, Student):
#         print("The salary is: ", obj.get_salary())
#     else:
#         raise TypeError("Unknown object")


objs = Student()
# get_status(obj)

# duck typing in the python is a programming concept where the type  
#or the class of an objectis less important than the methods it have
#when we use duck typing we do not check types at all instead you check for the presence of a 
# given method or attribute 

l = (1,2,3,4,5)
print(type(l))
t = [1,2,3,4,5]
print(type(t))
d = {1:2 , 2:4 , 4:8}
print(type(d))

def get_value(obj):
    if(isinstance(obj,(list,tuple))):
        for i in t:
            print(i , end = "  ")
        print()
    else :
        raise TypeError("Unknown class")

get_value(l)
get_value(t)
# get_value(d)
get_value(objs)
