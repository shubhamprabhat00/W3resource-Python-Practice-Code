# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

random_string = input("Enter a Sentence: ")
n_times = int(input("Enter the number of times you want to print the sentence: "))

for x in range(n_times):
    print(random_string)