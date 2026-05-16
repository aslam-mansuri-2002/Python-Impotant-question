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

