# # TUPLE
# myTuple = ("Gilligan", "Cataway", "red")
#
# for m in myTuple:
#     print(m)
#
# # Strings
# myString = "It was the best of times."
# for char in myString:
#     print(char, end="")
#
# # Range in loop will help with index in loops
# for i in range(len(myString)):
#     print(i)
#     print(myString[i])
#
# # Using enumerate
# for i, item in enumerate(myString):
#     print(f"{i}:{item}")
#
# # What index is this value at in a list?
# # You can use the index in String or List
# print(f"{myString.index('i')}")
import math


# Dictionary

# bestOFXF = {
#     "2x1": "Clyde Bruckman's Final Repose",
#     "2x2": "War of the Coprohages",
#     "2x3": "Jose Chung's From Outer Space"
# }

# for key in bestOFXF:
#     print(key)
#     # print(bestOFXF[key])
#     # "Check out Episode ___or '___.'"
#     print(f"Check out Episode {key} or '{bestOFXF[key]}.'")


# FILL THE BASKET/ ACCUMULATOR ... FILTER
# word = "Clyde Bruckman's Final Repose"
# newWord = word.split()
# myList = ["Clyde", "Bruck man",'s', 'Final Repose']
# newContainer = []
# for item in myList:
#     if item.find("s"):
#         newContainer.append(it
#
#         em)
# print(newContainer)

# 1. getting a string of input
# userInput = input("get values: ")
# newList = userInput.strip().split()
# # newList = ["Alfred", "Arrey-Ndip", "Bate"]
#
# value = newList[1]
# middle_initial = value[0]
# # print(middle_initial)
# print(f"{newList[-1]}, {newList[0]}. {middle_initial}")

# 2. Getting a list of input
# myInput = input("Please enter your number of names?  ")
#
# num = int(myInput)
# nameList = []
#
# for i in range(0, num):
#     nextInput = input("Get next name: ")
#     nameList.append(nextInput)
#
# second_word = nameList[1]
# middle_name = second_word[0]
# print(f"{nameList[-1]},{nameList[0]} {middle_name}." )

# Lab 33.15
# last_four_digits = 8005551212 % 10000
# print(8005551212 % 1000000)


# def numSquared(num):
#     return math.pow(num, 2)
#
#
# if __name__ == "__main__":
#     userInput = int(input("Please enter a value: "))
#     result = numSquared(userInput)
#     sentence = "The square of {} is {}".format(userInput, result)
#     print(sentence)
# print(dir(__builtins__))
help(list.append)