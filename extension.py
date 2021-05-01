"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""


def main():
    steps = 0
    n = int(input("Enter a number: "))
    while n !=1:
        steps += 1
        if (n%2 == 0):
            new_n = int(n / 2)
            print(str(n)+" is even, so I take half: "+str(new_n))
            n = int(new_n)
        else:
            new_n = 3 * n + 1
            print(str(n) + " is odd, so I take 3n+1: " + str(new_n))
            n = int(new_n)
    print("The process took "+str(steps)+" steps to reach "+str(n))



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
