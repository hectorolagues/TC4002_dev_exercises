# Master in Computer Science
# TC4002 Analysis, Design and Construction of Software
# Lab 1 - Exercise 2 - Converter
# Command line program that take as input a number and
# then it displays in the console corresponding number
# (positive integers plus zero) in Binary and Hex. It
# manages errors with exceptions for not using numbers
# Author: Héctor Gabriel Olagues Torres
# Date: 16/February/2021
# Version: 0.1.beta
# Email: A00354877@itesm.mx

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


test_values = ["-1", "0", "10", "11", "123456"]

print("Exercise 2 - CONVERTER")

index = 0
for value in test_values:
    index = index + 1
    print("\n\nTest {0}: Value {1}".format(index, value))
    # Condition to check whether the input paramter contains only numeric digits
    if value.isdecimal():
        # Only numeric digits
        input_value = int(value)
        # Print the numbers in Binary and Hexadecimal format
        print("\nInput value parameter in Binary: ")
        decimalToBinary(input_value)
        print("\n\nInput value parameter in Hexadecimal: ")
        print("0x", end="")
        decimalToHex(input_value)
    else:
        # There is one or more digits that are not numeric
        print("\nThe input parameter does not contain only numeric digits")

input("\n\nPress type any key to exit")
