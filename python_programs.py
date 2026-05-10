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

#--> 9 Write a Python program to solve quadratic equation.

# The standard form of a quadratic equation is:
# 2
# 𝑥
# 𝑎 +𝑏𝑥+𝑐=0
# where
# a, b and c are real numbers and
# 𝑎 ≠ 0
# The solutions of this quadratic equation is given by:
# 2
# 𝑏
# (−𝑏 ± ( −4𝑎𝑐 )/(2𝑎)
# )1/

import math

a = float(input("Enter corfficient a :-"))
b = float(input("Enter corfficient b :-"))
c = float(input("Enter corfficient c :-"))

# Calculate the discriminant

disc = b**2 - 4*a*c

# chek discr... is zero, negtive or possitive
if disc > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif disc == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(disc)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i") 

#-->.10 Write a Python program to swap two variables without temp variable.
a = 62 
b = 23 
a,b=b,a
print(f"a= {a} hai and b= {b} hai")

# --> 11 Write a Python Program to Check if a Number is Positive, Negative or Zero

num = float(input("Enter number :- "))
if num > 0:
    print(f"{num} number is possitive")
elif num < 0:
    print(f"{num} this number is negaitive")
else:
    print(f"{num} this is zero, nothing")

# ---> 12 Write a Python Program to Check if a Number is Odd or Even
num = int(input("enter number :- "))

if num%2==0:
    print(f"{num} is EVEN number")
else:
    print(f"{num} is  ODD number")

# ---> 13 Write a Python Program to Check Leap Year

year = int(input("Enter year :-"))

if year%400==0 and year%100==0:
    print(f"{year} is leap year ")
elif year%4==0 and year%100 != 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is NOT leap year")

#--->14 Write a Python Program to Check Prime Number

num = int(input("ENTER YOU'R NUMBER :- "))
flag = False
if num <= 1:
    flag = True
elif num > 1:
    for i in range(2,num):
        if num%i==0:
            flag = True
            break
else:
    flag = False
if flag:
    print(f"{num} is NOT prime")
else:
    print(f"{num} is PRIME")

#--> 15 Write a Python Program to Print all Prime Numbers in an Interval of 1-10

lower = 1
upper = 10
only_prime_num = []

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            only_prime_num.append(num)
print(only_prime_num)

# --> 16 Write a Python Program to Find the Factorial of a Number.

num = int(input("Enter number :- "))
factorial = 1
if num < 0:
    print(f"{num} negative number ka factorial nahi nikal sakta ")
elif num == 0:
    print(f"{num} ka factorial 1 hai")
else:
    for i in range(1,num+1):
        factorial = factorial*i
print(f"{num} ka factorial hai {factorial}")

# --> 17 Write a Python Program to Display the multiplication Table

table_num = int(input("Enter number of table :- "))
for i in range(1,11):
    print(f"{table_num} X {i} = {table_num*i}")

# --> 18. Write a Python Program to Print the Fibonacci sequence

n_terms = int(input("kitne terms tak aapko sequence chahiye :- "))
n1 = 0
n2 = 1
count = 0
if n_terms <= 0:
    print("please possitive number dale")
elif n_terms == 1:
    print(f"fibonacci sequence up to {n_terms}")
else:
    print("fibonacci squence")
    while count < n_terms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1

# -->19. Write a Python Program to Check Armstrong Number
num = int(input("Enter number :-"))
num_order = len(str(num))
sum_total = 0
tem_num = num

while 0 < tem_num:
    digit = tem_num%10
    digit = digit**num_order
    sum_total += digit
    tem_num = tem_num//10

if num == sum_total:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is NOT Armstrong")

# --> 20 Write a Python Program to Find Armstrong Number in an Interval

starting_num = int(input("Enter Starting number :- ")) 
ending_num = int(input("Enter Ending number :- "))

for num in range(starting_num,ending_num+1):
    num_order = len(str(num))
    sum_total = 0
    tem_num = num
    while 0 < tem_num:
        digit = tem_num%10
        digit = digit**num_order
        sum_total += digit
        tem_num = tem_num//10
    if num == sum_total:
        print(f"{num} is Armstrong")

# -->21. Write a Python Program to Find the Sum of Natural Numbers.

n = int(input("Enter the limit :- "))
if n < 1:
    print(f"{n} not allowd , please enter upper to 1")
else:
    # n*(n+1)/2 aa ak sutar se badha nutral number nu sum karva mate
    sum_n = n*(n+1)//2 
    print(sum_n)

