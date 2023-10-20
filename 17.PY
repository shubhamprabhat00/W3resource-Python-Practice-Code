# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def numwithIn(num):
    if(num < 100):
        return 100
    elif(num >= 100 and num < 1000):
        return 1000
    elif(num >= 1000 and num <2000):
        return 2000
    else:
        return "out of range"


num = int(input("Enter the number"))
print("The number is within", numwithIn(num))