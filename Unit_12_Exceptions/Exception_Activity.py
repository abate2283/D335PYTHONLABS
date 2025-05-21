# 7
# 9
# 3
# 4
# q
user_input = input("Please enter a number: ")
while user_input != 'q':
    try:
        number = int(user_input)
        print(number * 2)
    except:
        print('x')
    user_input = input()
print('e')