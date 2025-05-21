user_input = int(input("Please enter a number: "))
pattern = ""
hashTag = ""
odd = user_input % 2 == 1
even = user_input % 2 == 0
i = 0
while i <= 10:
    if 0 <= (user_input <= 10) and (user_input == odd):
        user_input = "*"
        pattern += user_input
        user_input = int(input("Please enter a number "))
        i += 1
    if user_input == even:
        user_input = "*"
        hashTag += user_input
        user_input = int(input("Please enter a number "))
        i += 1

else:
    print("Completed")
print(pattern)
print(hashTag)
