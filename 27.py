# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 27. Write a Python program that concatenates all elements in a list into a string and returns it.

lista = ['S','h','u','b','h','a','m']

newStr = ''

for i in lista:
    newStr = newStr + i

print(f'Data Type of the input: ',type(lista))
print(f'Data Type of the Output: ',type(newStr))

print(f'New String: ',newStr)
