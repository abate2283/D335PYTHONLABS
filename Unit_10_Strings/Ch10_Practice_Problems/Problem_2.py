# Write a program that reads email addresses until -1.
# Print only emails that contain exactly one @ and end with .com.
#
# Example Input:
#
# john@example.com
# invalid@domain
# hello@world.net
# user123@gmail.com
# -1
# Expected Output:
#
# john@example.com
# user123@gmail.com
prompt = "Enter an email: "
while True:
    validEmail = input(prompt)
    if validEmail == "-1":
        break
    if validEmail.count("@") == 1 and validEmail.endswith(".com"):
        print(validEmail)

#