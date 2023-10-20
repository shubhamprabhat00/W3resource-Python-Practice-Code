# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php



# 21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.


num = int(input("Enter a number to determine Even/Odd "))

if num > 0 and num % 2 == 0:
    print("Number is Even")
elif num > 0 and num % 2 == 1:
    print("Number is Odd")
elif num <= 0:
    print("Number is not valid for the Odd/Even determination")