# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
# Sample Output:
# print(sum_three(2, 1, 2))
# print(sum_three(3, 2, 2))
# print(sum_three(2, 2, 2))
# print(sum_three(1, 2, 3))

# 0
# 0
# 0
# 6  

def sum(a,b,c):
    if(a == b or b == c or a == c):
        return 0
    else:
        return a+b+c

print(f"sum of the numbers are: ",sum(2,1,2))
print(f"sum of the numbers are: ",sum(3,2,2))
print(f"sum of the numbers are: ",sum(2,2,2))
print(f"sum of the numbers are: ",sum(1,2,3))

