"""
File: nimm.py
-------------------------
Add your comments here.
"""
import random

def main():
    stones = 20
    player = 1
    while stones > 0:
        print("There are "+str(stones)+" stones left")
        turn = input("Player "+str(player)+" would you like to remove 1 or 2 stones? ")
        while (turn != '2' and turn != '1') or (int(turn) > stones):
            turn = input("Please enter 1 or 2: ")
        stones -= int(turn)
        if player == 1:
            player = 2
        else:
            player = 1
        print("")
    print("Player "+str(player)+" wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
