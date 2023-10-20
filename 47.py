# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 47. Write a Python program to find out the number of CPUs used.
import os

print(os.cpu_count())



import multiprocessing
print(multiprocessing.cpu_count())