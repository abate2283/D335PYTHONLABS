myList = [2, 3, 4, 7, 9, 8, 11]


def get_user_num1():
    result =0
    try:
        for r in myList:
            if r > len(myList):
                raise IndexError("Index out of bounds!")
            result += r * 2
            print(result)
    except IndexError as e:
        print("Error", e)






def compute_avg(user_num1, user_num2):
    print("FIXME: Finish compute_avg()")
    return -1


user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num1()
user_num2 = get_user_num1()
avg_result = compute_avg(user_num1, user_num2)

# print(f"Average: {avg_result}")
