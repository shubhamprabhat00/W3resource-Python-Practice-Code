# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.


str_s = input("Enter a string:")
n_times = int(input("Enter how many time you want to repeat"))
str_new = ""
for x in range(n_times):
    str_new = str_new + str_s[:2]

print(str_new)