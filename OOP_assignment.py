#  Mixed OOP + Polymorphism + Abstraction

# 31. Create an abstract class Shape with abstract method area() → make Square 
# & Circle classes.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2 
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
square = Square(5)
circle = Circle(3) 
print(f"Area of square: {square.area()}")
print(f"Area of circle: {circle.area()}")

# 32. Payment gateway class banao: pay() method override in UPI, Card, 
# Netbanking. 
from abc import ABC, abstractmethod
class Payment_geteway(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment_geteway):
    def pay(self,amount):
        print(f"Paid ${amount} using UPI (GPay/PhonePe)")
class Card(Payment_geteway):
    def pay(self,amounnt):
        print(f"Paid ${amounnt} using Card (debit/credit)")
class Netbanking(Payment_geteway):
    def pay(self,amount):
        print(f"Paid ${amount} using Netbanking")

a = UPI()
b = Card()
c = Netbanking()

my_list = [a,b,c]

for i in my_list:
    i.pay(100)

# 33. School system banao: Teacher & Student same showInfo() method use kare 
# (polymorphism).

class schoolMember:
    def __init__(self,name):
        self.name = name
    def showInfo(self):
        pass
class teacher(schoolMember):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject
    def showInfo(self):
        print(f"Teacher name: {self.name} | Subject name: {self.subject}")
class student(schoolMember):
    def __init__(self, name ,std):
        super().__init__(name)
        self.std = std
    def showInfo(self):
        print(f"Student name: {self.name} | std.. {self.name}")
member = [teacher("anita ma'am","English"),student("ahad saikh","10th")]
for i in member:
    i.showInfo()

# 34. Function overloading jaisa effect create karo (default parameters use 
# karke).

class boy:
    def boyInfo(self,name,age=None):
        if age is not None:
            print(f"Boy name : {name} | Boy age {age}")
        else:
            print(f'boy name is {name}')

rohan = boy()
rohan.boyInfo("rohan makvana")
rohan.boyInfo("rohan makvana",16)

# 35. Create a class Vehicle → override start() in Bike & Car classes. 

class vehicle:
    def start(self):
        pass
class bike(vehicle):
    def start(self):
        print("Bike start ho rahi hai")
class car(vehicle):
    def start(self):
        print("Car start ho rahi hai")

my_bike = bike()
my_bike.start()
my_car = car()
my_car.start()

'''|--->36. Encapsulation + Polymorphism use karke Employee bonus calculation logic 
banao.<----|'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def getSalary(self):
        return self.__salary
    def cal_bonus(self):
        pass
class manager(Employee):
    def cal_bonus(self):
        bonus = self.getSalary() * 0.20
        return f"manegar name : {self.name} aapka bonus {bonus}"
class developer(Employee):
    def cal_bonus(self):
        bonus = self.getSalary() * 0.10
        return f"developer name : {self.name} aapka bonus {bonus}"

my_Employee = [manager("aman dhat",50000),developer("rohan kumar",30000)]
for i in my_Employee:
    i.cal_bonus()

# 37. Abstraction use karke Database class banao: MySQL & MongoDB classes 
# implement connect(). 

from abc import ABC, abstractmethod
class database(ABC):
    @abstractmethod
    def connect(self):
        pass
class MySQL(database):
    def connect(self):
        return "connecting to MySQL database.."
class MongoDB(database):
    def connect(self):
        return "connecting to MangoDB database.."
    
db1 = MySQL()
db1.connect()
db2 = MongoDB()
db2.connect()

# 38. Polymorphism use karke animalSound() function banao Dog, Cat, Cow ke 
# sath. 

class Animal:
    def animalSound(self):
        pass
class Dog(Animal):
    def animalSound(self):
        return "bhaw bhaw"
class Cat(Animal):
    def animalSound(self):
        return "meow meow"
class Cow(Animal):
    def animalSound(self):
        return "moo moo"

animal = [Dog(),Cat(),Cow()]
for i in animal:
    i.animalSound()

# 39. Inheritance + constructor chaining (super()) ka example banao. 
class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def studentInfo(self):
        print(f"stundet name : {self.name} | stundet roll number : {self.roll_number}")

class student_1(student):
    def __init__(self, name, roll_number):
        super().__init__(name, roll_number)

rohan = student_1("rohan bhat",208)
rohan.studentInfo()

# 40. Industry-level e-commerce model banao:

from abc import ABC, abstractmethod
class paymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(paymentGateway):
    def pay(self, amount):
        return f"UPI se {amount} transfer huve"
# ------------- data hide karna --- Encapsulation
class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price
    def get_base_price(self):
        return self.__price
    def cal_bill(self):
        return self.get_base_price()
# ------------- Inhertace karna aur polymorphism karna 
class Electronics(Product):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def cal_bill(self):
        tax = self.get_base_price()*0.18
        return self.get_base_price()+tax
    
class Clothing(Product):
    def __init__(self, name, price,discount):
        super().__init__(name, price)
        self.discount = discount
    def cal_bill(self):
        discount = self.get_base_price() * (self.discount / 100)
        return self.get_base_price() - discount
    
#------- yaha se mai kaam hoga 
  
p1 = Electronics("Mobail",50000,"2 Years")
p2 = Clothing("T shirt",1000,10)

cart = [p1,p2]
total_amount = 0
for item in cart:
    finel_price = item.cal_bill()
    print(f"Item: {item.name} and Finel price is (tax or discount ke baad) {finel_price}")
    total_amount += finel_price

print("-" * 50)
print(f"Total Bill: ₹{total_amount}")

# Payment process
payment_service = UPI()
print(payment_service.pay(total_amount))

