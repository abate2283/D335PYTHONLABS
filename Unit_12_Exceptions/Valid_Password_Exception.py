valid_password = False
while valid_password == False:
    try:
        password = input()
        if len(password) < 8:
            raise ValueError("Invalid")
        valid_password = True
        print("Valid")
    except ValueError as excpt:
        print(excpt)


# user_input = ''
# while user_input != 'q':
#     try:
#         user_input = int(input())
#         if user_input < 0:
#             raise ValueError("Invalid")
#         print(f'Value: {user_input}')
#
#     except ValueError as excpt:
#         print(excpt)
#