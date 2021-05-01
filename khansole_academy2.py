"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    correct = 0
    while correct < 3:
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print("What is "+str(num1)+" + "+str(num2)+"?")
        answer = num1 + num2
        guess = int(input("Your answer: "))
        if int(answer) == int(guess):
            correct += 1
            print("Correct! You've gotten "+str(correct)+" correct in a row.")
        else:
            correct = 0
            print("Incorrect. The expected answer is "+str(answer))
    print("Congratulations! You mastered addition.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
