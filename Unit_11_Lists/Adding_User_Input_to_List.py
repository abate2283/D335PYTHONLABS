# 20 30 56 12 45 200 inputs
user_input = input("Enter a valid number: ")
token = user_input.split()
numberList = []
for index, variable in enumerate(token):
    numberList.append(int(variable))
    print(f"Index {index} : Variable {variable}")

for i in numberList:
    average = sum(numberList) // len(numberList)
    print(f" Average: {average}")
