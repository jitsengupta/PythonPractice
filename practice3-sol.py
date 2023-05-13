"""
practice3.py - create a loop that asks
for user input continuously and creates an instance of a class
with that input as before. But this time if the
user types in something like "bye" then you should
end the program.

Start by copying and pasting the code from practice2
below, then add the loop and the conditions

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



if __name__ == '__main__':
    pass

    # Do a bit of CFC here - what should be the logic?
    
    # how long do we loop?
    while True:
        # inside the loop, what do we do in each pass?
        myname = input("What is your name? ")

        # when the user types bye quit the loop
        if myname.lower() == 'bye':
            break
        myinstance = SomeClass(myname)
        print(myinstance)
