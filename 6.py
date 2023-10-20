# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

sample_data = "3, 5, 7, 23"
list = sample_data.split(",")

print(type(list))
print(f'List:',list ,'\n')

tuple = tuple(list)
print(type(tuple))
print(f'Tuple:',tuple)