# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.


def sum(a,b):
    if(a+b > 15 and a+b <=20 ):
        return 20
    else:
        return a+b

print(f"sum of the numbers are: ",sum(10,6))
print(f"sum of the numbers are: ",sum(10,2))
print(f"sum of the numbers are: ",sum(10,12))
print(f"sum of the numbers are: ",sum(1,2))