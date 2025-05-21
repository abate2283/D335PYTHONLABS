user_input = int(input("Please enter a number: "))
while user_input != 'q':
    try:
        number = user_input
        print(number * 2)
    except:
        print("x")
    user_input = int(input("Please enter a number: "))
print("e")

prompt = "Enter a value:\n"
user_input = int(input(prompt))
while user_input != "q":
    try:
        number = user_input * 2
        print(number)
    except:
        print("You entered q..")
    user_input = int(input(prompt))
print("Exit")
