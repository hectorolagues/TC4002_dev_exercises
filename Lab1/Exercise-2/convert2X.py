##########################################################
## Master in Computer Science                           ##
## TC4002 Analysis, Design and Construction of Software ##
##########################################################
## Lab 1 - Exercise 2 - Converter                       ##
## Command line program that take as input a number and ##
## then it displays in the console corresponding number ##
## (positive integers plus zero) in Binary and Hex. It  ##
## manages errors with exceptions for not using numbers ##
##########################################################
## Author: Héctor Gabriel Olagues Torres                ##
## Date: 16/February/2021                               ##
## Version: 0.1.beta                                    ##
## Email: A00354877@itesm.mx                            ##
##########################################################

# This function converts from decimal format to Binary format
def decimalToBinary(numDecimal):
    if numDecimal > 1:
        # Recursive approach
        decimalToBinary(numDecimal // 2)
    print(numDecimal % 2, end="")
    
# This function converts from decimal format to Hexadecimal format
def decimalToHex(numDecimal):
    if numDecimal > 15:
        # Recursive approach
        decimalToHex(numDecimal // 16)
    tempVal = numDecimal % 16
    if tempVal < 10:
        print(tempVal, end="")
    if tempVal == 10:
        print("A", end="")
    if tempVal == 11:
        print("B", end="")
    if tempVal == 12:
        print("C", end="")
    if tempVal == 13:
        print("D", end="")
    if tempVal == 14:
        print("E", end="")
    if tempVal == 15:
        print("F", end="")


print("Exercise 2 - CONVERTER")

inputString = input("\nPlease type a positive integer number, including zero: ")

# Condition to check whether the input paramter contains only numeric digits
if inputString.isdecimal():
    # Only numeric digits
    inputValue = int(inputString)
    # Condition to check only positive integers are converted, including zero
    if inputValue < 0:
        print("\nOnly positive integers (plus zero) are allowed")
    else:
        # Print the numbers in Binary and Hexadecimal format
        print("\nInput value parameter in Binary: ")
        decimalToBinary(inputValue)
        print("\n\nInput value parameter in Hexadecimal: ")
        print("0x", end="")
        decimalToHex(inputValue)
else:
    # There is one or more digits that are not numeric
    print("\nThe input parameter does not contain only numeric digits")

input("\n\nPress type any key to exit")
