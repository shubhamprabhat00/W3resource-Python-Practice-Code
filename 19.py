# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
# Click me to see the sample solution

input_string = input("Enter somthing\n")

def check(input_string):
    if(len(input_string) >= 2 and 'ls' == input_string[0:2] ):
        return input_string
    else:
        return 'ls' + input_string

print(check(input_string))