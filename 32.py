# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 32. Write a Python program to find the least common multiple (LCM) of two positive integers.

# Output: (4, 6) -> 12
#         lcm(15, 17)) -> 255


num1 = 15
num2 = 17

if(num1 > num2):
    num = num1
elif(num2 > num1):
    num = num2
elif(num1 == num2):
    print(f"LCM of ",num1," and ",num2, " is: ",num1)


while(True):
    if(num % num1 == 0 and num % num2 == 0):
        LCM = num
        break
    else:
        num = num + 1 

print(f"LCM of ",num1," and ",num2, " is: ",LCM)
