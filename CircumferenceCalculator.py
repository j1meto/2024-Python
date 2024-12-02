#Written by Jimeto Onyeabo on 2nd December 2024.
#This piece of code calculates the circumference of a circle
#The equation for the circumference of a circle is pi * diameter

import math

print("The circumference of the circle will be outputted as an integer ( rounded to the nearest whole number)")

#This program takes an input from the user (the diameter) to calculate the circumference
#have to convert the input to integer
diameter = int(input("Enter in the diameter: "))
#Calm lil calculating statement
print("Calculating...")
pi = math.pi
#Variable that holds the value of circumference and makes it an integer
circumference = int(diameter*pi)

print(f"The circumference of the circle is {circumference}")
