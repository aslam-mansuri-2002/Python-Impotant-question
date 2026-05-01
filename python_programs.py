#-->1  Write a Python program to print "Hello Python"
print("Hello")

#-->2.1 Write a Python program to do arithmetical operations addition and division.

num_1 = float(input("Enter frist number :- "))
num_2 = float(input("Enter seconde number :- "))
sum = num_1 + num_2
print(sum)

#-->2.2  Division
num_1 = float(input("Enter frist number :- "))
num_2 = float(input("Enter seconde number :- "))
if num_2 == 0:
    print("Division zero se nahi ho sakta")
else:
    division = num_1/num_2
    print(division)

# --> 3 Write a Python program to find the area of a triangle

base = float(input("Enter you'r base:- "))
height = float(input("Enter you'r height:- "))
    # calculate the area of a triangle
area = 0.5*base*height
print(area)

# --> 4 Write a Python program to swap two variables

a = 5
b = 10
temp = 0
temp = a
a = b
b = temp
print(f"a-->{a}|b--> {b}")

# --> 5 Write a Python program to generate a random number

import random
print(f"random number:-{random.randint(1,100)}")

# --> 6 Write a Python program to convert kilometers to miles.

kilometers = float(input("Enter distance in kilometers:"))
con_factor = 0.621371
miles = kilometers*con_factor
print(f"{kilometers} kilometers is equle to {miles} miles")

# --> 7 Write a Python program to convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print (f"{celsius} degrees Celsius is equal to {fahrenheit} degrees fahrenheit")

# --> 8 Write a Python program to display calendar

import calendar
y = int(input("enter year :-"))
m = int(input("enter month :-"))
cal = calendar.month(y,m)
print(cal)

