# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hai-Jaha Tatham
# Date: 9/23/26
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# Creates a variable x, and set its value to an number from the user
print("please enter a whole number: ")
x = input()

# Checks type of variable
print(type(x))

# Type of x is str so it is converted to int instead
x = int(x)

# If statement evaluates whether x is greater than or equal to 6
if x >= 6:
    print("x is greater than 6")

elif x >= 4 and x < 12:
    print("x is greater than 4 and smaller than 12")