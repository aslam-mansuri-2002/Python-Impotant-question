# --> 109 Create a function that returns the thickness (in meters) of a piece of paper after
# folding it n number of times. The paper starts off with a thickness of 0.5mm.
'''Examples
num_layers(1) 
➞ "0.001m"- Paper folded once is 1mm (equal to 0.001m)
num_layers(4) 
➞ "0.008m"- Paper folded 4 times is 8mm (equal to 0.008m)
num_layers(21) 
➞ "1048.576m"- Paper folded 21 times is 1048576mm (equal to 1048.576m)'''


def num_layers(n):
    thickness_mm = 0.5 *(2**n)
    thickness_m = thickness_mm/1000
    return f"{thickness_m}m"

num_layers(1)
num_layers(4)

# --> 110 Create a function that takes a single string as argument and returns an ordered list
# containing the indices of all capital letters in the string
'''Examples
index_of_caps("eDaBiT") 
➞ [1, 3, 5]
index_of_caps("eQuINoX") 
➞ [1, 3, 4, 6]
index_of_caps("determine") 
➞ []
index_of_caps("STRIKE") 
➞ [0, 1, 2, 3, 4, 5]
index_of_caps("sUn") 
➞ [1]'''

def index_of_caps(word):
    return [ i for i,j in enumerate(word) if j.isupper()]

index_of_caps("eDaBit")
index_of_caps("AslaM")
index_of_caps("mansurI")

# --> 111 Using list comprehensions, create a function that finds all even numbers from 1 to
# the given number
'''find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]'''

def find_even_n(n):
    return [ i for i in range(1,n+1) if i%2==0]

find_even_n(10)

# --> 112 Create a function that takes a list of strings and integers, and filters out the list so
# that it returns a list of integers only. 
'''Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", 1729]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []'''

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

# --> 113 Given a list of numbers, create a function which returns the list but with each
# element's index in the list added to itself. This means you add 0 to the number at
# index 0, add 1 to the number at index 1, etc...
'''add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]'''

def add_indexes(my_list):
    return [i+num for i,num in enumerate(my_list)]

add_indexes([0,0,0,0,0])
add_indexes([1,2,3,4,5])

# --> 114 Create a function that takes the height and radius of a cone as arguments and returns
# the volume of the cone rounded to the nearest hundredth. See the resources tab for
# the formula.
'''cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0'''

import math
def cone_volume(height, radius):
    if radius == 0:
        return 0
    volume = (1/3) * math.pi * (radius**2) * height
    return round(volume, 2)

cone_volume(3,2)

# ---> 115
'''This Triangular Number Sequence is generated from a pattern of dots that form a
triangle. The first 5 numbers of the sequence, or dots, are:
1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the
third one has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number
of the sequence.
Examples
triangle(1) ➞ 1
triangle(6) ➞ 21
triangle(215) ➞ 23220'''

def triangle(n):
    return (n*(n+1))//2

triangle(6)
triangle(215)

# --> 116 Create a function that takes a list of numbers between 1 and 10 (excluding one
# number) and returns the missing number.
'''missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7'''

def missing_num(lst):
    return 55 - sum(lst)

missing_num([1,2,3,5,6,7,8,9,10]) #output : 4

# --> 117 Write a function that takes a list and a number as arguments. Add the number to the
# end of the list, then remove the first element of the list. The function should then
# return the updated list
'''next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
next_in_line([], 6) ➞ "No list has been selected'''

def next_in_line(lst,num):
    if not lst:
        return "No list has been selected"
    lst.append(num)
    lst.pop(0)
    return lst

next_in_line([1,2,3,4],5)
next_in_line([],1)

# --> 118  Create the function that takes a list of dictionaries and returns the sum of people's
# budgets.
'''Examples
get_budgets([
{ 'name': 'John', 'age': 21, 'budget': 23000 },
{ 'name': 'Steve', 'age': 32, 'budget': 40000 },
{ 'name': 'Martin', 'age': 16, 'budget': 2700 }
]) ➞ 65700'''

def get_budget(lst):
    return sum([i["budget"] for i in lst])

dict_list = [
   {"name":"john","age":21,"budget":23000},
   { 'name': 'Steve', 'age': 32, 'budget': 40000 },
   { 'name': 'Martin', 'age': 16, 'budget': 2700 }
]

get_budget(dict_list)

# ---> 119 Create a function that takes a string and returns a string with its letters in
# alphabetical order
'''alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("edabit") ➞ "abdeit"
alphabet_soup("hacker") ➞ "acehkr"'''

def alphabet_soup(txt):
    return "".join(sorted(txt))

alphabet_soup("hello")
alphabet_soup("mansuri")

# ---> 120 
'''Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded
monthly. What will be the value of your investment at the end of the 10 year period?
Create a function that accepts the principal p, the term in years t, the interest rate r,
and the number of compounding periods per year n. The function returns the value at
the end of term rounded to the nearest cent.
For the example:
compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
Note that the interest rate is given as a decimal and n=12 because with monthly
compounding there are 12 periods per year. Compounding can also be done
annually, quarterly, weekly, or daily.
Examples
compound_interest(100, 1, 0.05, 1) ➞ 105.0
compound_interest(3500, 15, 0.1, 4) ➞ 15399.26'''

def compound_interest(p, t, r, n):
    # 1. Formula
    final_amount = p * ((1 + (r / n)) ** (n * t))
    return round(final_amount, 2)

print(compound_interest(10000, 10, 0.06, 12))  
print(compound_interest(100, 1, 0.05, 1))      
print(compound_interest(3500, 15, 0.1, 4))     

# --> 121 Write a function that takes a list of elements and returns only the integers
'''return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]
return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20,3]'''

def only_int(lst):
    return [ i for i in lst if isinstance(i,int)]

only_int([9,2,"space","car","lione",16,22])

# ---> Program 122
'''Create a function that takes three parameters where:- x is the start of the range (inclusive).- y is the end of the range (inclusive).- n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third
parameter n
Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []'''

def list_operation(x,y,n):
    return [ i for i in range(x,y+1) if i%n==0 ]

list_operation(1,10,3)
list_operation(7,9,2)

# --> 123 Create a function that takes in two lists and returns True if the second list follows the
# first list by one element, and False otherwise. In other words, determine if the second
# list is the first list shifted to the right by 1.
'''simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes:- Both input lists will be of the same length, and will have a minimum length of 2.- The values of the 0-indexed element in the second list and the n-1th indexed
element in the first list do not matter'''

def simon_says(lst1,lst2):
    return lst1[:-1]==lst2[1:]

simon_says([1,2],[5,5])
simon_says([1,2,3],[3,5,6]) #<--
simon_says([1,2,3,4,5],[0,1,2,3,4])

# --> 124 A group of friends have decided to start a secret society. The name will be the first
# letter of each of their names, sorted in alphabetical order. Create a function that takes
# in a list of names and returns the name of the secret society

'''society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"'''

def society_name(name_lst):
    return "".join(sorted([i[0] for i in name_lst]))

society_name(["Aslam","Rahil","Shahrukh","Masud"])

# --> 125 An isogram is a word that has no duplicate letters. Create a function that takes a
# string and returns either True or False depending on whether or not it's an "isogram"
'''is_isogram("Algorism") ➞ True
is_isogram("PasSword") ➞ False- Not case sensitive.
is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings'''

def is_isogram(word):
    lower_word = word.lower()
    return len(lower_word) == len(set(lower_word))

is_isogram("Algorism")
is_isogram("PasSword")

# --> 126 Create a function that takes a string and returns True or False, depending on whether
# the characters are in order or not.
'''is_in_order("abc") ➞ True
is_in_order("edabit") ➞ False
is_in_order("123") ➞ True
is_in_order("xyzz") ➞ True'''

def is_in_order(txt):
    return txt == "".join(sorted(txt))

is_in_order("abc")
is_in_order("edabit")

# --> 127 Create a function that takes a number as an argument and returns True or False
# depending on whether the number is symmetrical or not. A number is symmetrical
# when it is the same as its reverse
'''Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True'''

def is_symme(n):
    txt = str(n)
    return txt == txt[::-1]
is_symme(7227)

# --> 128 Given a string of numbers separated by a comma and space, return the product of
# the numbers
'''Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20'''

def multiply_num(txt):
    num_lst = txt.split(",")
    product = 1
    for i in num_lst:
        product *= int(i)
    return product

multiply_num("2,3")
multiply_num("1,2,3,4")

# --> 129 Create a function that squares every digit of a number
'''Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer'''

def square_digits(num):
    result = ""
    for i in str(num):
        sq = int(i)**2
        result += str(sq)

    return int(result)
    
square_digits(9191)
square_digits(3212)

# --> 130 Create a function that sorts a list and removes all duplicate items from it
'''setify([1, 3, 3, 5, 5]) ➞ [1,3,5]  
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]'''

def setify(lst):
    return list(set(sorted(lst)))

setify([3,3,3,2,1])
setify([1,3,3,5,5])

# --> 131 Create a function that returns the mean of all digits
'''Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
The mean of all digits is the sum of digits / how many digits there are (e.g. mean
of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be an integer'''

def mean(num):
    total_sum = sum([int(i) for i in str(num)])
    return total_sum//len(str(num))

mean(42)
mean(12345)

# --> 132 Create a function that takes an integer and returns a list from 1 to the given number,
# where:
'''1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
number).
2. If the number cannot be divided evenly by 4, simply return the number.
Examples
amplify(4) ➞ [1, 2, 3, 40]
amplify(3) ➞ [1, 2, 3]
amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21,
22, 23, 240, 25]
Notes
The given integer will always be equal to or greater than 1.
Include the number (see example above).
To perform this problem with its intended purpose, try doing it with list
comprehensions. If that's too difficult, just solve the challenge any way you can.'''

def amplify(num):
    return [i*10 if i%4==0 else i for i in range(1,num+1)]

amplify(25)
amplify(4)

# --> 133 Create a function that takes a list of numbers and return the number that's unique.
'''Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0  
Notes
Test cases will always have exactly one unique number while all others are the same.'''

def unique(lst):
    return [x for x in lst if lst.count(x)==1][0]

unique([3,3,3,7,3])
unique([0,0,0.77,0,0])

# ---> Program 134
'''Your task is to create a Circle constructor that creates a circle with a radius provided
by an argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter
(circumference).
For help with this class, I have provided you with a Rectangle constructor which you
can use as a base example.
Examples
circy = Circle(11)
circy.getArea()
Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
Should return 27.897342763877365
Notes
Round results up to the nearest integer.'''

import math
class Circal:
    def __init__(self,r):
        self.r = r
    def getArea(self):
        result = math.pi * (self.r**2)
        return round(result,3)
    def getPrimeter(self):
        result = 2*math.pi*self.r
        return round(result,3)

c = Circal(11)
c.getArea()

# -->  135 Create a function that takes a list of strings and return a list, sorted from shortest to
# longest.
'''Examples
sort_by_length(["Google", "Apple", "Microsoft"]) ➞ ["Apple", "Google", "Microsoft"]
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) ➞ ["Raphael","Leonardo", "Donatello", "Michelangelo"]
sort_by_length(["Turing", "Einstein", "Jung"]) ➞ ["Jung", "Turing", "Einstein"]
Notes
All test cases contain lists with strings of different lengths, so you won't have to deal'''

def sort_by_length(lst):
    return sorted(lst,key=len)

sort_by_length(["google","apple","microsoft"])

# -->136 Create a function that validates whether three given integers form a Pythagorean
# triplet. The sum of the squares of the two smallest integers must equal the square of
# the largest number to be validated
'''Examples
is_triplet(3, 4, 5) ➞ True 
3² + 4² = 25
5² = 25
is_triplet(13, 5, 12) ➞ True
5² + 12² = 169
13² = 169
is_triplet(1, 2, 3) ➞ False
1² + 2² = 5
3² = 9
Notes
Numbers may not be given in a sorted order'''

def is_triplet(a,b,c):
    n = sorted([a,b,c])
    return (n[0]**2)+(n[1]**2) == (n[2]**2)

is_triplet(13,5,12)
is_triplet(1,2,3)

# --> 137 Create a function that takes three integer arguments (a, b, c) and returns the amount
# of integers which are of equal value
'''Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3.'''

def equal(a,b,c):
    if a==b==c:
        return 3
    elif a==b or b==c or a==c:
        return 2
    else:
        return 0

equal(3,2,3)
equal(1,1,1)

# --> 138 Write a function that converts a dictionary into a list of keys-values tuples
'''Examples
dict_to_list({"D": 1,"B": 2"C": 3}) ➞ [("B", 2), ("C", 3), ("D", 1)]
dict_to_list({"likes": 2,"dislikes": 3,"followers": 10}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
Notes
Return the elements in the list in alphabetical order.'''

def dict_to_list(d):
    return sorted(d.items())

dict_to_list({"d":1,"b":2,"c":3})

