def getWeight():
    user_weight = int(input("Enter your weight: "))
    if user_weight < 0:
        raise ValueError("Invalid Weight!")
    return user_weight


def getHeight():
    user_height = int(input("Enter your height: "))
    if user_height < 0:
        raise ValueError("Invalid Height!")
    return user_height


user_input = ""
while user_input != "q":
    try:
        height = getHeight()
        weight = getWeight()
        BMI = (float(weight) / float(height * height)) * 703
        print(f"Your BMI is: {BMI:.2f}")
        print('(CDC: 18.6-24.9 normal)\n')
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')
    user_input = input("Press any key or q to quit: ")

