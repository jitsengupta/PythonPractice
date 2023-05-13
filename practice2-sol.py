"""
practice2.py - Ask for input from the user and
Then create an instance of a class with that input
Start by copying and pasting the code from practice1
below, then ask for the user's name and create an
instance of your class with that name

paste your code below. This file is pretty much empty.

"""
"""
A simple 2 method class - almost all classes should have
these two methods - a constructor and a string converter
that allows you to print this class with some meaningful
information - useful for debugging
"""

class SomeClass:

    """
    A constructor (__init__) for our class - feel free to change the name
    above. Say this class takes a name parameter and sets it to
    its attribute. Can you set a default value of the name if
    no attribute is passed?
    """
    def __init__(self, cname = 'Jit'):
        self._name = cname
        
    """
    A string converter (__str__) for our class. Get this method
    to return a string of the form "My name is [name attribute]"
    """
    def __str__(self):
        return f"My name is {self._name}"

"""
This should be in your file. You can actually have this in every
Python file you create - gives you a simple way to test out the stuff
in this file (or anything thi sfile imports
"""

if __name__ == '__main__':
    
    # create a couple instance of your class above, one where you
    # send a parameter, one where you don't and print both instances
    # in separate print statements
    myname = input("What is your name? ")
    myinstance = SomeClass(myname)
    print(myinstance)

"""
To get user input, call the input function with a prompt.
Make sure you have a space or some other ending character
like a : so you can distinguish between your prompt and
what the user typed in. e.g.:
myname = input("What is your name? ")
"""
