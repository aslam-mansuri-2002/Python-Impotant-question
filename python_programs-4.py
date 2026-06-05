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

