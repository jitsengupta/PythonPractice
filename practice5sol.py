"""
practice5.py - This is our final practice file. We are
going to build a simple guessing game here. The computer
randomly selects a number between 0 and 100 (or a range
provided as a parameter), then repeatedly asks the user
to guess the number. If the user guess is too high, the
program says that it is too high. If the user guess is
too low, it responds appropriately. If the user guesses
correctly, it will then congratulate and let the user
know how many attempts it took for the user to guess it.

You can start with the Game class in Practice4.
What attributes should this class need?

In the main part of the app, ask the user repeatedly
to enter a number. Then respond saying if the number
is higher or lower than the stored number.

Quit the program when the user types in a negative number.
You can report how many tries before the user quit, and
what the number was that the program thought of.

"""
import random

class Game:

    """
    A constructor (__init__) for our class - feel free to change the name
    above. Say this class takes a name parameter and sets it to
    its attribute. Can you set a default value of the name if
    no attribute is passed?
    """
    def __init__(self, cnumber = 0):
        self._attempts = 0
        if cnumber == 0:
            self._number = random.randint(1,100)
        else:
            self._number = cnumber
        
    """
    checkGuess takes the nubmer the user typed in, and
    responds if the user typed in something higher or lower
    than the game number
    """
    
    def checkGuess(self, num):
        self._attempts = self._attempts + 1
        if num > self._number:
            print(f"Sorry {num} is too high")
            return False
        elif num < self._number:
            print(f"Sorry, {num} is too low")
            return False
        else:
            print(f"Congratulations, you got it in {self._attempts} tries!")
            return True
    
    """
    A string converter (__str__) for our class. Get this method
    to return a string of the form "My name is [name attribute]"
    """
    def __str__(self):
        return f"The number is {self._number}"


if __name__ == '__main__':
    myinstance = Game()
    print(myinstance)

    # Do a bit of CFC here - what should be the logic?
    
    # how long do we loop?
    while True:
        # inside the loop, what do we do in each pass?
        mynumber = input("Guess a number: ")

        n = int(mynumber)
        # when the user types -1 quit the loop
        if n < 1:
            break
        
        # Check if the number was too low or high
        if myinstance.checkGuess(n):
            break
