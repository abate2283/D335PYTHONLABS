prompt = "Enter a value:\n"
userEntry = int(input(prompt))

try:
    if userEntry < 0:
        raise ValueError('Wrong Value???')
    value = userEntry * 2
    print(value)

except ValueError as e:
    print("Error Occurred!!!", e)

print("BYE")

#  This two codes are the same one uses an input and a while loop the other one does not.

prompt1 = "User value:\n"
userInput = int(input(prompt1))
while userInput != "q":
    try:
        value = 2 // userEntry
        if value == 0:
            raise ZeroDivisionError("UserEntry should not be zero!!")
        print(value)
    except ValueError as e:
        print("Error", e)
    userInput = int(input(prompt1))

print("Bye...")
