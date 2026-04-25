# class
# 21. Create a class Student with name and marks; print grade based on marks.

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def show_grade(self):
        if self.marks >= 85:
            print(f"dear student {self.name} you'r marks is {self.marks} and you'r greade is A")
        elif self.marks >= 65:
            print(f"dear student {self.name} you'r marks is {self.marks} and you'r greade is B")
        elif self.marks >= 45:
            print(f"dear student {self.name} you'r marks is {self.marks} and you'r greade is C")
        elif self.marks >= 35:
            print(f"dear student {self.name} you'r marks is {self.marks} and you'r greade is D")
        else:
            print(f"dear student {self.name} you'r marks is {self.marks} and you'r FAIL")

rohan = student("rohan makvana",55)
rohan.show_grade()

# 22. Bank Account class banao: deposit, withdraw, check balance methods. 

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            print(f"rs.{amount} jama ho gaye , new balance hai {self.balance}")
        else:
            print("please sahi se amount dale")
    def withfraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"rs.{amount} aapke account se nikale gaye, new balance hai {self.balance}")
        else:
            print("please sahi se amount dale, paisa balance se jayada hai")
    def chek_balance(self):
        print(f"aapke account mai mojuda , rs.{self.balance}")

my_account = BankAccount("Ahad saikh",1000)
my_account.deposit(1000)
my_account.chek_balance()
my_account.withfraw(500)

# 23. Car class banao: company, model input lo → print info. 

class Car:
    def __init__(self,company,model):
        self.company = company
        self.model = model
    def get_info(self):
        print("_______Car infometion_______")
        print(f"company hai {self.company}")
        print(f"model hai {self.model}")

company = input("car ki company batayi yah: ")
model = input("car ki model batayi yah: ")

my_car = Car(company,model)
my_car.get_info()


# 24. Employee class banao encapsulation ke sath (private salary). 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def chek_salary(self):
        print(f"Mr.{self.name} ki salary {self.__salary} hai")

sameer = Employee("sameer ansari",20000)
sameer.chek_salary()

# 25. Rectangle class banao area & perimeter calculate karne ke liye. 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

l = float(input("Rectangle ki lambai (Length) likhein: "))
w = float(input("Rectangle ki chaudai (Width) likhein: "))

my_rect = Rectangle(l, w)

print(f"Rectangle ka Area hai: {my_rect.calculate_area()}")
print(f"Rectangle ka Perimeter hai: {my_rect.calculate_perimeter()}")

# 26. A program using single inheritance (Person → Student).

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f"student name is {self.name} and age is {self.age}")
class Student(Person):
    def __init__(self, name, age,seat_no,center):
        super().__init__(name, age)
        self.seat_no = seat_no
        self.center = center
    def student_info(self):
        self.person_info()
        print(f"you're seat number is {self.seat_no} and you're center is {self.center}")

mukesh = Student("mukesh sing",25,10235,"M K Gandhi College")
mukesh.student_info()
mukesh.person_info()

# 27. Program using multi-level inheritance (Animal → Dog → Puppy).

class Animal:
    def eat(self):
        print("Animal is eat food")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Puppy(Dog):
    def cry(self):
        print("Puppy is crying")

tomy = Puppy()
tomy.bark()
tomy.eat()
tomy.cry()


