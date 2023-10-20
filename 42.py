# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import platform

a= platform.architecture()
b = platform.win32_edition()
print(a)
print(b)
print(platform.machine())