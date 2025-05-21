getInput = int(input("Enter value: "))
num = 3
while getInput != "q":
    try:
        value = int(input("Enter value: "))
        print(value * num)
    except ValueError as e:
        print(e)
    getInput = int(input("Enter value: "))
print("Exception!!")

# 6
# R
# i
# q