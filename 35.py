# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.



def sum(a,b):
    if(a == b or a+b == 5 or a-b == 5):
        return True
    else:
        return False

print(f"Numbers are: ",sum(7,2))
print(f"Numbers are: ",sum(3,2))
print(f"Numbers are: ",sum(2,2))
print(f"Numbers are: ",sum(7,3))
print(f"Numbers are: ",sum(27,53))
