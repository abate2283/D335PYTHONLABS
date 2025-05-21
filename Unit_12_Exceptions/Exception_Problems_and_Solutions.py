# Write a program that reads two integers: a and b, and outputs a % b. Use exception handling to catch:
# Division by zero.
# Invalid input types.

prompt = "Enter an integer:\n"
try:
    a = int(input(prompt))
    b = int(input("Enter next integer:\n"))

    solution = a % b
    print(solution)

except ZeroDivisionError as e:
    print("Zero Division Exception:",e)
except ValueError as e:
    print("Input Exception:", e)