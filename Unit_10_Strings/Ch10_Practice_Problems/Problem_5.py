# 🆔 Problem 5: Filter User IDs
#
# Prompt:
#
# Write a program that reads user IDs until -1.
# Print only those that are exactly 8 characters long and start with an uppercase letter.
#
# Example Input:
#
# JohnDoe1
# Jane2022
# ALPHA123
# bobby456
# -1
#
# Expected Output:
#
# ALPHA123

try:
    prompt = "Please enter a password: "
    while True:
        password = input(prompt)
        if password == "-1":
            break
        if (len(password) == 8 and password.isalnum()
                and password[0].isupper() and
                password.count(password[0]) == 1 and password.isspace() == False and password.isdecimal() == False):
            print(password)

except ValueError as e:
    print(e)
