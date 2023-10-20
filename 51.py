# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 51. Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for 
# how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

import timeit
def sum():
    print(1+2)

print(timeit.timeit())  
