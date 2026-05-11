# --> 31 Write a Python Program for cube sum of first n natural numbers

n = int(input("Enter the value of n :"))
if n <= 0:
    print("please Enter the possitive number")
else:
    cube_sum = sum([i**3 for i in range(1,n+1)])
    print(cube_sum)

