# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# Sample Output:

# GCD of 12 & 17 = 1
# GCD of 4 & 6 = 2
# GCD of 336 & 360 = 24


num1 = 336
num2 = 360

for i in range(1,int(num1/2)):
    if(num1 % i == 0 and num2 % i == 0):
        GCD = i
print(f"GCD of ",num1," and ",num2, " is: ",GCD)