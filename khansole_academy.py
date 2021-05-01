"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("What is"+str(num1)+"+"+str(num2)+"?")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
