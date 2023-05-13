"""
practice4.py - We are going to build a little game
today in the final practice app, but before we go there,
let's do something simple.

Create a Game class, similar to the class before, but
this class has a number instead of a name

In the main part of the app, ask the user repeatedly
to enter a number. Then respond saying if the number
is higher or lower than, a randomly generated number

Make this application as Object-oriented as you can.
Create the game class with the number 100 (or have the game class
randomly generate a number if no number is specified)

Have a method in the game class that makes the decision
about higher or lower and print the info.

Quit the program when the user types in a negative number.

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
        if num > self._number:
            print(f"Sorry {num} is too high")
        else:
            print(f"Sorry, {num} is too low")
    
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
        # when the user types bye quit the loop
        if n < 1:
            break
        
        # Check if the number was too low or high
        print(myinstance)
        myinstance.checkGuess(n)
