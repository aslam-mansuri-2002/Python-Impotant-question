# --> 72 Write a Python program to check order of character in string using OrderedDict().

from collections import OrderedDict
def check_order(input_string, pattern):
    ordered_dict = OrderedDict.fromkeys(input_string)
    pattern_index = 0

    for char in ordered_dict:
        if char == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index == len(pattern):
                return True

    return False

check_order("hello world", "hlo") 

# -->73 Write a Python program to sort Python Dictionaries by Key or Value

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
# sort by value
sorted_by_value = {k: v for k, v in sorted(sample_dict.items(), key=lambda item: item[1])}
print("Sorted by value:", sorted_by_value)

# --> 74 Write a program that calculates and prints the value according to the given formula:
'''𝑄=Square root of 2𝐶𝐷/H
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma
separated sequence.
Example
Let us assume the following comma separated input sequence is given to the
program:
100,150,180'''

import math
d = "100,150,180"
c = 50
h = 30
d_values = d.split(",")
q_values = []

for i in d_values:
    q = math.sqrt(2*c*int(i)/h)
    q_values.append(q)

str_q = ",".join(str(round(q)) for q in q_values)
print(str_q)

# --> 75 
'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''

'''aasan bhasa mai isme karna yah ki hum 2D array banayenge jisme rows ki sankhya X hogi aur columns ki sankhya Y hogi. Har element ka value i*j hoga, jahan i row index hai aur j column index hai.'''

x, y = 3, 5
array_2d = [[i * j for j in range(y)] for i in range(x)]
print(array_2d)

# --> 76 Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
'''sawal ka matlab hai ki hum ek string lenge jisme words comma se alag honge, unhe sort karenge aur phir sorted words ko comma se alag karke print karenge.'''

str_input = input("Enter a comma separated sequence of words: ")
words = str_input.split(",")
sorted_words = sorted(words)
sorted_str = ",".join(sorted_words)
print(f"real sentence:- {str_input} || sorted sentence :- {sorted_str}")

# --> 77 Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically
'''sawal ka matlab hai ki hum ek string lenge jisme words whitespace se alag honge, unme se duplicate words ko remove karenge, unhe sort karenge aur phir sorted unique words ko print karenge.'''

input_str = "hello word hello python and javascript and python"
output = " ".join(sorted(set(input_str.split())))
print(output)

# --> 78 Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program

word = "hello world! 123"
letters = 0
digit = 0
for char in word:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digit += 1
print(f"letters: {letters} || digits: {digit}")

# --> 79 is missing

# --> 80 ------------ 
'''Program 80
A website requires the users to input username and password to register. Write a
program to check the validity of password input by users. Following are the criteria
for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria are to
be printed, each separated by a comma''' 

import re

user_input = "ABd1234@1,aslam100$,mansuri100"
passwords_list = user_input.split(",")
valid_password = []

for p in passwords_list:
    if not (6 <= len(p) <= 12):
        print(f"{p} is invalid because of length")
        continue

    has_letter = False
    has_number = False
    has_special_char = False

    for char in p:
        if char.islower():        
            has_letter = True
        elif char.isdigit():      
            has_number = True
        elif char in "$#@":    
            has_special_char = True

    if not has_letter:
        print(f"{p} is invalid because of letter")
    elif not has_number:
        print(f"{p} is invalid because of number")
    elif not has_special_char:
        print(f"{p} is invalid because of special character")
    else:
        valid_password.append(p)

valid_password_str = ",".join(valid_password)
print(f"\nvalid passwords are:- {valid_password_str}")

# --> 81 Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n

class DivisibleBySeven:
    def __init__(self,n):
        self.n = n
    def generate(self):
        for i in range(self.n+1):
            if i % 7 == 0:
                yield i

ob = DivisibleBySeven(50)
for j in ob.generate():
    print(j)

# --> 82 Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically. Suppose the following input is
# supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or
# Python 3.

'''Then, the output should be:
2:2 - 3.:1 - 3?:1 - New:1 - Python:5 - Read:1 - and:1 - between:1 - choosing:1 - or:2 - to:1'''

input_str = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
word_record = {}
for w in input_str.split():
    if w in word_record:
        word_record[w] += 1
    else:
        word_record[w] = 1

word_record = dict(sorted(word_record.items()))
print(word_record)

# --> 83 Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class

class Person:
    def getGender(self):
        pass
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"

boy = Male()
boy.getGender()
girl = Female()
girl.getGender()

# --> 84 Please write a program to generate all sentences where subject is in ["I", "You"] and
# verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

subjects = ["I" , "You" ]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]

for i in subjects:
    for j in verbs:
        for k in objects:
            print(f"{i} {j} {k}")

# --> 85 Please write a program to compress and decompress the string "hello world!hello
# world!hello world!hello world!"

'''zlib ak module hai jo data compression aur decompression ke liye use hota hai. Hum is module ka use karke string ko compress karenge aur phir usko decompress karenge.'''

import zlib

my_str = b"hello world!hello world!hello world!hello world!"
print(my_str)
compressed_str = zlib.compress(my_str)
print(compressed_str)
decompressed_str = zlib.decompress(compressed_str)
print(decompressed_str)

# --> 86 Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list

def binary_search(arr,target):
    sorted_arr = sorted(arr)
    low = 0
    high = len(sorted_arr)-1

    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return target
        elif sorted_arr[mid] < target:
            low = mid +1
        else:
            high = mid - 1
    
    return -1

my_list = [1, 3, 6, 7, 4, 5,2]
print(binary_search(my_list, 4))


