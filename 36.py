# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 36. Write a Python program to add two objects if both objects are integers.



def sum(a,b):
    if(a.isdigit() == True and b.isdigit() == True):
        print(int(a)+ int(b))
    else:
        print("Input must be Integers")

input1 = input("Enter 1st number")
input2 = input("Enter 2nd number")
sum(input1,input2)
print(type(input1))
