##########################################################
## Master in Computer Science                           ##
## TC4002 Analysis, Design and Construction of Software ##
##########################################################
## Lab 1 - Exercise 1 - Find the number                 ##
## Command line program that generates a random number  ##
## between 1 and 30 (including 1 and 30), asks the user ##
## to guess the number and outputs whether they guessed ##
## too low, too high, or exactly right.                 ##
##########################################################
## Author: Héctor Gabriel Olagues Torres                ##
## Date: 16/February/2021                               ##
## Version: 0.1.beta                                    ##
## Email: A00354877@itesm.mx                            ##
##########################################################

# Libraries
from random import randint

print("Exercise 1 - Find the number")

# Initialize the guesses counter
guesses = 0

# Generate random number between 1 and 30
randomNum = randint(1, 30)

inputValue = ""
inputValueInt = 0
while inputValue != "exit" and inputValueInt != randomNum:
    # Ask the user to guess the number
    print("\nGuess the number generated randomly. It should be between >= 1 and <= 30.")
    inputValue = input("Please type the number: ")
    if inputValue != "exit":
        inputValueInt = int(inputValue)
        # Check if the number is within the accepted range
        if inputValueInt < 1:
            print("\nThe number should be >= 1.")
        elif inputValueInt > 30:
            print("\nThe number should be <= 30.")
        else:
            # Check whether the guess was too low, too high, or exactly right
            if inputValueInt > randomNum:
                print("\nYour guess was too high")
            elif inputValueInt < randomNum:
                print("\nYour guess was too low")
            else:
                print("\nYour guess was exactly right")
        # Increment the number of guesses
        guesses += 1

# Print the number of guesses the user has taken
print("\nNumber of guesses the user has taken: %d" %guesses)

# Store the number of guesses the user has taken in a file named GuessingSteps.txt
guessesString = str(guesses)
file = open("GuessingSteps.txt", "w")
file.write(guessesString)
file.close()

input("\nPress type any key to exit")
