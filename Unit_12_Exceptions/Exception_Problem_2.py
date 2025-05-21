# Write a program that reads a number and prints its square root.
# If the user enters a negative number, output an error message.
# Catch any non-numeric input using try-except.
import math

try:
    a = float(input("Enter a number:\n"))
    if a < 0:
        raise ValueError("Error number cannot be negative!")
    result = math.sqrt(a)
    print(result)
except ValueError as e:
    print("Input Exception:",e)
