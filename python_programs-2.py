# --> 31 Write a Python Program for cube sum of first n natural numbers

n = int(input("Enter the value of n :"))
if n <= 0:
    print("please Enter the possitive number")
else:
    cube_sum = sum([i**3 for i in range(1,n+1)])
    print(cube_sum)

# -->32 Write a Python Program to find sum of array

arr = [1,2,3]
print(sum(arr))

# -> for loop ke sath
total_sum = 0
for i in arr:
    total_sum += i
print(total_sum)


# --> 33 Write a Python Program to find largest element in an array
my_arr = [10,20,99,30]
largest_num = my_arr[0]

for i in my_arr:
    if i > largest_num:
        largest_num = i
print(f"{my_arr} ke andar largest number {largest_num} hai")

# --> 34 Write a Python Program for array rotation

def rotate_arr(my_list,d):
    n = len(my_list)
    d = d%n
    rotate_arr = my_list[d:]+my_list[:d]
    return rotate_arr
my_arr = [1,2,3,4,5]
rotate_arr(my_arr,6)

# --> 35 Write a Python Program to Split the array and add the first part to the end

def split_arr(my_list,d):
    n = len(my_list)
    d = d%n
    frist = my_list[:d]
    seconde = my_list[d:]
    result =  seconde + frist
    return result

my_arr = [10,20,30,40,50]
split_arr(my_arr,9)

# --> 36  Write a Python Program to check if given array is Monotonic

'''Pehle iska matlab samajhte hain. Monotonic ka matlab hota hai ki array ya to sirf badh raha hai (Increasing) ya sirf ghat raha hai (Decreasing). Beech mein rasta badalna mana hai!
exp--> [1,2,3,3,4,5]--> monotonic hai
exp --> [5,4,3,3,1] --> monotonic hai
exp --> [1,5,2,1,9] --> monotonic nahi hai '''

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            decreasing = False
        elif arr[i] > arr[i+1]:
            increasing = False
    
    if increasing or decreasing:
        print(f"{arr} monotonic hai")
    else:
        print(f"{arr} monotonic nahi hai")

my_arr = [1,2,3,3,7,5]
print(is_monotonic(my_arr))

# --> 37 Write a Python Program to Add Two Matrices.
'''Pehle samajhte hain ki matrix kya hota hai. Matrix ek 2D array hota hai, jisme rows aur columns hote hain. Jab hum do matrices ko add karte hain, toh hum unke corresponding elements ko add karte hain.
exp -->
Matrix A: [[1, 2], [3, 4]]
Matrix B: [[5, 6], [7, 8]]
Matrix C (A + B): [[6, 8], [10, 12]]'''

# Matrix X (Size: 3 Rows, 3 Columns)
X = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

# Matrix Y (Size: 3 Rows, 3 Columns)
Y = [
    [9, 8, 7],  # Row 0
    [6, 5, 4],  # Row 1
    [3, 2, 1]   # Row 2
]

# Ek khali matrix jawab store karne ke liye (Shuruat mein sab 0 hai)
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# 1. Bahar wala loop (Rows ke liye)
for i in range(len(X)):  # len(X) = 3, to i chalega 0, 1, 2
    
    # 2. Andar wala loop (Columns ke liye)
    for j in range(len(X[0])):  # len(X[0]) = 3, to j chalega 0, 1, 2
        
        # Aamne-saamne wale elements ko jod rahe hain
        result[i][j] = X[i][j] + Y[i][j]

# Jawab dekhne ke liye
for row in result:
    print(row)

# --> 38 Write a Python Program to Multiply Two Matrices.
'''Matrix multiplication thoda alag hota hai. Jab hum do matrices ko multiply karte hain, toh hum pehle matrix ke rows ko dusre matrix ke columns ke saath multiply karte hain aur unka sum nikalte hain.'''

# Matrix X (Size: 3x3)
X = [
    [1, 2],
    [4, 5],
    [7, 8]
]

# Matrix Y (Size: 2x3)
Y = [
    [1, 2, 3],
    [4, 5, 6]
]

# Jawab store karne ke liye khali matrix (Size: 3x3)
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# 1. Pehla Loop: X ki Rows ke liye
for i in range(len(X)):
    # 2. Doosra Loop: Y ke Columns ke liye
    for j in range(len(Y[0])):
        # 3. Teesra Loop: Multiplication ke liye (Common size)
        for k in range(len(Y)):
            result[i][j] = result[i][j] + (X[i][k] * Y[k][j])

# Jawab Print karne ke liye
print("Matrices ka Multiplication hai:")
for row in result:
    print(row)

# --> 39 Write a Python Program to Transpose a Matrix
'''Matrix ka transpose karna matlab hota hai ki uske rows aur columns ko swap kar dena. Matlab, jo pehle row tha, wo ab column ban jayega, aur jo pehle column tha, wo ab row ban jayega.'''

# Original Matrix (3 Rows, 2 Columns)
X = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = [
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(X)):     
    for j in range(len(X[0])):   
        result[j][i] = X[i][j]

print("Matrix ka Transpose hai:")
for row in result:
    print(row)

# --> 40 Write a Python Program to Sort Words in Alphabetic Order
sentence = input("Enter a sentence :")
a = sentence.split()
a.sort()
shorted_sentence = " ".join(a)
print(shorted_sentence)

# --> 41 Write a Python Program to Remove Punctuation From a String
'''Punctuation marks jaise ki comma (,), period (.), exclamation mark (!), question mark (?), aur aise hi aur bhi symbols hote hain jo humare sentences mein hote hain. Jab hum punctuation ko remove karte hain, toh hum in symbols ko apne string se hata dete hain, taki sirf words bache.'''

import string
def remove_punctuation(input_string):
    symbols = string.punctuation
    result = "".join(char for char in input_string if char not in symbols)
    return result

remove_punctuation("!!aslam# mansuri , how@@ are you????/ ")

# -> 42 is balnk

# -> 43 Write a Python program to check if the given number is a Disarium Number
'''Disarium number wo hota hai jisme har digit ka position ke hisab se power nikal ke unka sum original number ke barabar hota hai jes ki 135 ek disarium number hai kyunki 1^1 + 3^2 + 5^3 = 135'''

num1 = int(input("Enter a number :"))
numtostr = str(num1)
total_sum = 0
for i,d in enumerate(numtostr):
    total_sum += int(d)**(i+1)

if total_sum == num1:
    print(f"{num1} ek Disarium number hai")
else:
    print(f"{num1} ek Disarium number nahi hai")

# --> 44 Write a Python program to print all disarium numbers between 1 to 100

for i in range(1,101):
    convert_num = str(i)
    total_sum = 0
    for p,d in enumerate(convert_num):
        total_sum += int(d)**(p+1)
    if total_sum == i:
        print(i)

# --> 45  Write a Python program to check if the given number is Happy Number
'''Happy number wo hota hai jisme aap us number ke digits ka square nikal ke unka sum karte hain, aur phir us sum ka bhi digits ka square nikal ke unka sum karte hain, aise hi process repeat karte hain. Agar aapko 1 milta hai, toh wo number happy number hota hai. Agar aapko 4 milta hai, toh wo number unhappy number hota hai.'''

def chek_happy_number(num):
    
    original_num = num
    num_list = []

    while num != 1 and num not in num_list:
        num_list.append(num)
        num = sum(int(digit)**2 for digit in str(num))
    if num == 1:
        print(f"{original_num} ek Happy number hai")
    else:
        print(f"{original_num} ek Happy number nahi hai")

chek_happy_number(19)

# --> 46 Write a Python program to print all happy numbers between 1 and 100

num_1to100 = [num for num in range(1,101)]

for num in num_1to100:
    num_set = set()
    ori_num = num
    while num != 1 and num not in num_set:
        num_set.add(num)
        num = sum(int(d)**2 for d in str (num))
    if num == 1:
        print(ori_num)
        
# --> 47 Write a Python program to determine whether the given number is a Harshad
# Number.

'''Harshad number wo hota hai jisme aap us number ke digits ka sum nikal ke us original number ko us sum se divide karte hain. Agar division ka result ek integer hota hai, toh wo number Harshad number hota hai.jese ki 18 ek harshad number hai kyunki 1 + 8 = 9 aur 18 ko 9 se divide karne par result 2 aata hai, jo ek integer hai. in short, agar aapka number apne digits ke sum se perfectly divide ho jata hai, toh wo Harshad number hai.'''

my_num = int(input("Enter a number :"))

num_sum = sum(int(d) for d in str(my_num))
if my_num % num_sum == 0:
    print(f"{my_num} ek Harshad number hai")
else:
    print(f"{my_num} ek Harshad number nahi hai")

# -->48 Write a Python program to print all pronic numbers between 1 and 100
'''Pronic number wo hota hai jisme aap kisi integer n ko uske next integer (n+1) se multiply karte hain. Agar aapko apne original number ke barabar result milta hai, toh wo number pronic number hota hai. jese ki 6 ek pronic number hai kyunki 2 x 3 = 6, aur 2 aur 3 consecutive integers hain. iska ak formula hota hai n*(n+1)'''

for num in range(1,101):
    pronic_num = num*(num+1)
    if pronic_num < 100:
        print(pronic_num)

# --> 49 sum of list elements
my_list = [1,2,3,4,5]
total_sum = 0
for i in my_list:
    total_sum += i

# --> 50 Write a Python program to Multiply all numbers in the list
my_list = [1,2,3,4,5]
total_product = 1
for i in my_list:   
    total_product *= i 
print(total_product)

# --> 51 Write a Python program to find smallest number in a list.
numbers = [30, 10, -45, 5, 20]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(f"{numbers} ke andar smallest number {smallest} hai")

# --> 52 Write a Python program to find  largest number in a list.
numbers = [30, 10, -45, 5, 20]
big_num = numbers[0]
for i in numbers:
    if i > big_num:
        big_num = i
print(f"{numbers} ke andar largest number {big_num} hai")

# --> 53 Write a Python program to find second largest number in a list.
numbers = [30,30,10,11,50]
frist_largest = second_largest = float('-inf')
for i in numbers:
    if i > frist_largest:
        second_largest = frist_largest
        frist_largest = i
    elif i > second_largest and i != frist_largest:
        second_largest = i
print(f"{numbers} ke andar second largest number {second_largest} hai") 

# -> 54 Write a Python program to find N largest elements from a list
n = 3
num = [30, 10, 45, 5, 20, 99, 8]
unique_num = list(set(num))
unique_num.sort(reverse=True)
n_num = unique_num[:n]
print(f"{num} ke andar {n} largest number {n_num} hai")

# --> 55 Write a Python program to print even numbers in a list
numbers = [30, 10, 45, 5, 20, 99, 8]
even_numbers = [i for i in numbers if i%2==0]
print(even_numbers)

# --> 56 Write a Python program to print odd numbers in a List

numbers = [30, 10, 45, 5, 20, 99, 8]
odd_numbers = [i for i in numbers if i%2!=0]
print(odd_numbers)

# --> 57 Write a Python program to Remove empty List from List.


list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
cleaned_list = [l for l in list_of_lists if l]
print(f"Original list: {list_of_lists} and cleaned list: {cleaned_list}")

# --> 58 Write a Python program to Cloning or Copying a list.

original_list = [1,2,3,4]
copy_list = original_list[:]
copy_list.append(5)
print(f"Original list: {original_list} and copy list: {copy_list}")

# agr ham sirf = ka use kaege to copy nahi hoga 
list1 = [1,2,3,4]
list2 = list1
list2.append(5)
print(f"yaha pe farak nahi hoga kyunki list1 aur list2 dono same list ko point kar rahe hain, toh original list bhi change ho jayegi. Original list: {list1} and copy list: {list2}")

# -> 59 Write a Python program to Count occurrences of an element in a list.

my_list = [1,1,2,3,4,1,5,2]
target = 1
count = 0
# with for loop
for i in my_list:
    if i == target:
        count += 1
print(f"{my_list} ke andar {target} ki occurrences {count} hai")

# shortcut with count method
print(my_list.count(target))

# -> 60 Write a Python program to find words which are greater than given length k.

words_list = ["aslam", "mansuri", "python", "programming", "is", "fun"]
k = 5
k_length_word = [w for w in words_list if len(w) > k]
print(f"original list: {words_list} and words greater than {k} length: {k_length_word}")

# -> 61 Write a Python program for removing iℎ𝑖 character from a string.
'''sawal ka matlab hai ki aapko ek string di jayegi aur aapko us string ke iℎ𝑖 character ko remove karna hai. Matlab, agar aapko string "hello world" di gayi hai aur i = 4, toh aapko 4th index (0-based indexing) pe jo character hai usko remove karna hai.'''

my = "mansuri"
i = 3
t1 = my[:i]
t2 = my[i+1:]
print(f"original str {my} and result str {t1+t2}")

# -> 62 Write a Python program to split and join a string

str = 'i am aslam mansuri and i am learning python'
str_list = str.split()
again_str = " ".join(str_list)

print(f"real str : {str}")
print(f"{"-"*30} after use split and join {"-"*30}")
print(f"str list : {str_list}")
print(f"again str : {again_str}")

# --> 63 Write a Python program to check if a given string is binary string or not

def chek_binary_str(a):
    allowed = "01"
    is_binary = True
    for i in a:
        if i not in allowed:
            is_binary = False
            break
    if is_binary:
        print(f"{a} ek binary string hai")
    else:
        print(f"{a} ek binary string nahi hai")

chek_binary_str("55652")
chek_binary_str("0001110101")

# -->64 Write a Python program to find uncommon words from two Strings.

str1 = "aslam mansuri is learning python"
str2 = "aslam khan is learning javascript"

set1 = set(str1.split())
set2 = set(str2.split())

uncommon_words = set1^set2
print(f"uncommon word : {uncommon_words}")

# -> 65 Write a Python program to find all duplicate characters in string.

str1 = "aslammansuri"
duplicate_char = []
for i in str1:
    if str1.count(i) > 1 and i not in duplicate_char:
        duplicate_char.append(i)
print(duplicate_char)

# -> 66 Write a Python Program to check if a string contains any special character

def chek_special_char(str1):
    has_special = False
    for i in str1:
        if not i.isalnum() and i != " ":
            has_special = True
            break
    if has_special:
        print(f"{str1} me special character hai")
    else:
        print(f"{str1} me special character nahi hai")

chek_special_char("aslam_mansuri")

# --> 67 Write a Python program to Extract Unique dictionary values

my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

unique_values = []

for i in my_dict.values():
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)

# --> 68 Write a Python program to find the sum of all items in a dictionary
my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

total_sum = 0
for i in my_dict.values():
    total_sum += i
print(total_sum)

# --> 69 Write a Python program to Merging two Dictionaries.

dict1 = {
    "a": 10,
    "b": 20
}
dict2 = {
    "c": 30,
    "d": 40
}
merged_dict = {**dict1, **dict2}
print(merged_dict)


