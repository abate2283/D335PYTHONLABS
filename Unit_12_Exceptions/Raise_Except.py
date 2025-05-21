prompt = "Please enter a value:\n"
value = int(input(prompt))
while value != "q":
    try:
        if value < 0:
            raise ValueError
        number = value * 2
        print(value)
    except ValueError as e:
        print("Error", e)
    # value = int(input(prompt))
print("OK")