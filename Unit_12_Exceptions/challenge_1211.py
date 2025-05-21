prompt = "enter a value:\n"
userInput = int(input(prompt))
while userInput != "q":
    try:
        value = userInput * 2
        print(value)
    except:
        print("WRONG VALUE!!!")
    userInput = int(input(prompt))
print("Exited")

