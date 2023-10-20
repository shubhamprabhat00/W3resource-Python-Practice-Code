# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 25. Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

values = [1, 5, 8, 3]

def fun(a):
    return a in values

print(fun(23))