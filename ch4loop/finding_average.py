cost = [20, 30, 40, 50, 60, 70]
total = 0

for value in cost:
    total += value
print(f"Average: {total / len(cost)}")


def swap_values(user_val1, user_val2, user_val3, user_val4):
    otherValue = user_val1
    user_val2 = otherValue


val1 = int(input("val1"))
val2 = int(input("val2"))
val3 = int(input("val3"))
val4 = int(input("val4"))
swap_values(val1, val2, val3, val4)
