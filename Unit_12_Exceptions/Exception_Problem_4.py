# Prompt the user to input weight and height
# and compute the Body Mass Index (BMI). Catch errors
# like zero or negative height and invalid inputs.
#
# Formula: BMI = weight / (height ** 2)
import math

try:
    w = int(input("Enter weight: "))
    h = int(input("Enter height: "))
    if w <= 0:
        raise ValueError("w should not be less than zero!")
    elif h <= 0:
        raise ValueError("h should not be less than zero!")
    bmi = w / (math.pow(h, 2))
    print(f"BMI, {bmi:.2f}")

except ZeroDivisionError as e:
    print("Zero Division Exception:", e)
except ValueError as e:
    print("Input Exception:", e)
