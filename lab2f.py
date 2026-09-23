# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

import sys
num_args = len(sys.argv) -1
if num_args < 2:
    print("The Script requires atleast 2 arguments, No arguments provided")
else:
    name=sys.argv[1]
    age=sys.argv[2]
    if num_args==3:
        print(f"Hi {name}, you are {age} years old and the script recieved {num_args} arguments.")
    else:
        print("Hi {name}, you are {age} years old and the script recieved {num_args} arguments.")
        