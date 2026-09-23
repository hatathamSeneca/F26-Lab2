# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file

import sys
print(sys.argv) # prints list of all arguments givent at command line when running our python file
print(len(sys.argv)) # tells us number of command line arguments the user provides from terminal
num_args = len(sys.argv) -1 #count number of arguments minus name of the file
if num_args < 2:
    print("The Script requires atleast 2 arguments, No arguments provided")
else:
    name=sys.argv[1]
    age=sys.argv[2]
    if num_args==2:
        print(f"Hi {name}, you are {age} years old and the script recieved exactly two arguments")
    else:
        print(f"Hi {name}, you are {age} years old and the script recieved exactly {num_args} arguments")
