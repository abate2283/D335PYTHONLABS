user_input = input("Please enter a phrase: ")


def slicing_a_string(result):
    x = user_input[:len(user_input) // 2]
    y = user_input[len(user_input) // 2:]
    result = ""
    if x > y:
        result = x
        print(result)
        return result
    else:
        result = y
        print(result)


slicing_a_string(user_input)

# my_str = 'http://reddit.com/r/python'
# # print(my_str[11:])
# # it.com/r/python
#
# protocol = 'http://'
# print(len(protocol))
