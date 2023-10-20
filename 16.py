# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php



# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.


def calculate(num):
    if num <= 17:
        return 17 - num
    else:
        return (num - 17)*2
    
num = int(input("Enter the number: "))
# print(type(num))
print(calculate(num))