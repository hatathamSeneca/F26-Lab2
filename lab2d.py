# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date: Learn how to use command line arguments.
# Purpose: .
# Usage: ./lab2d.py


# TO DO 1: copy the required lines from README.md to print version, platform, argv and the length of argv.
# run the script in the terminal using command: python ./lab2d.py


# TO DO 2: copy the required lines from README.md to print argv[0], argv[1] and argv[2]
# run the script using the following command: python lab2d.py maija Maija

import sys

print(sys.version) # prints version of python currently in use
print(sys.platform) # prints name of operating system
print(sys.argv) # prints list of all arguments givent at command line when running our python
print(len(sys.argv)) # tells us number of command line arguments the user provides from terminal
print(sys.argv[0]) # prints first argument, always the name of the script
print(sys.argv[1]) # prints second argument
print(sys.argv[2]) # prints third argument
print(len(sys.argv)) # tells us the number of command line arguments user provides from terminal