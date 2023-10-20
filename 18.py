# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.


num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

def sum(num1, num2, num3):
    if(num1 != num2):
        return num1 + num2 + num3
    elif(num1 == num2 == num3):
        return 3*num1
print("Sum of the 3 numbers are:",sum(num1,num2,num3))