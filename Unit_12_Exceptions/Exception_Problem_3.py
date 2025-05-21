# Write a program that reads three integers from the user and prints their sum.
# If any input is invalid, print how many valid inputs were given and their total sum.

try:

    a = [int(input("Enter x:\n")), int(input("enter y:\n")), int(input("enter z:\n"))]
    print("Sum", sum(a))
    for i in a:
        if i < 0:
            raise ValueError("Number is not a valid input")
        else:
            print(sum(a))

except ValueError as e:
    print("Input Exception:", e)