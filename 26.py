# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 26. Write a Python program to create a histogram from a given list of integers.

# Sample Input: 1,2,3,4,5,6,7

input1 = input("\nEnter integer with comma: ")
histogram = [int(item) for item in input1.split(',')]

print(f'\n',type(input1))
print(f'Input Integer: ',input1)

print(f'\n',type(histogram))
print('Histogram: ',histogram,'\n')


for i in histogram:
    for _ in range(i):
        print('*', end= '')
        # /print('*')
    print('')