# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

amt,years = 10000,7
interest = 3.5
future_value = amt*((1+(0.01*interest)) ** years)

print(format(future_value,".2f"))