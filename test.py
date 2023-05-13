from practice5sol import *

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
