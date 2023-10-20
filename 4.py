# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

radius = float(input("Enter radius of the circle"))
pie = 3.14
Area = pie*(radius*radius)

print(f'Area of the circle is: ',Area)

# ///Another Method/////

from math import pi
Area = pi*radius*radius
print(f'Area of the circle is: ',round(Area,2))