# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php



# 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

def date_fun(date1, date2):
    if date1 > date2:
        return date1 - date2
    else :
        return date2 - date1

date1 = date(2023,3,24)
date2 = date(1996,3,24) 

print(date_fun(date1, date2))
