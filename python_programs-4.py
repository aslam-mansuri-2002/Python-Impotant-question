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

