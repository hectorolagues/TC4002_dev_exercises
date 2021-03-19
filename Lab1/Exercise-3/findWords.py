# Master in Computer Science
# TC4002 Analysis, Design and Construction of Software
# Lab 1 - Exercise 3 - FIND WORDS
# Program that parses a file given as parameter and
# counts the number of occurrences for a list of words
# identified in the file. The identification is case
# sensitive. The program will accept the words to test
# as arguments. English or Spanish.
# Author: Héctor Gabriel Olagues Torres
# Date: 16/February/2021
# Version: 0.1.beta
# Email: A00354877@itesm.mx


# Libraries
from os import path

# Functions
def countWords(fileContents, words):
    # Create a dictionary to count by word identified
    wordCoundDict = {}
    for word in words:
        wordCoundDict[word] = 0
    # Split the string of fileContents into a list
    wordsList = fileContents.split()
    # Iterate through the list of words
    for word in wordsList:
        # Increment in case a word from the list has been found in the dictionary
        if word in wordCoundDict:
            wordCoundDict[word] += 1
    # Return the dictionary to be printed along with the count of each key-value pair
    return wordCoundDict


print("Exercise 3 - COUNT WORDS")

# Input parameter indicating the path and name of the file
inputString = input("\nPlease type the path and name of the file to be parsed: ")
# Condition to check whether the path exists
if path.exists(inputString):
    # Open the file, read the contents and close it accordingly
    file = open(inputString, "r")
    fileRead = file.read()
    file.close()
    # Input parameter indicating the words to be counted
    inputWords = input("\nPlease type the words to be counted, separated by a space:\n")
    inputWordsList = inputWords.split()
    # Call the function that actually counts the words
    countResult = countWords(fileRead, inputWordsList)
    print(countResult)
else:
    # The path or the file are incorrect
    print("\nThe path and/or name of the file does not exist")

input("\nPress type any key to exit")
