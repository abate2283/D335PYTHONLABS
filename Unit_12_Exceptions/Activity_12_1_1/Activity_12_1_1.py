number = int(input())
try:
    while number != "q":
        number1 = int(input("Enter first number: "))
        print(number1 * 3)
        number2 = int(input("Enter second number: "))
        print(number2 * 4)
except ValueError as e:
    print("x", e)
    nextNumber = int(input("Enter next number: "))
print("ended")
