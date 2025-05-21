user_input = input("Please enter a number:")
# convert user_input to list
token = user_input.split()

num = []
for n in token:
    num.append(int(n))
    n += 1

for index in range(len(num)):
    value = num[index]
    print(f"{value}: {index}")
