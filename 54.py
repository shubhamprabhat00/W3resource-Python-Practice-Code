# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 52. Write a Python program to print to STDERR.

import getpass
print(getpass.getuser())

# Other Method

import os.path 

homedir = os.path.expanduser("~") 
print(homedir)