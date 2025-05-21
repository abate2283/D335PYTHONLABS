# Operators
# = # assigns
# == # equality ... asking a question, comparing, "are these equal?"
# +
# -
# *
# /
# % #  modulo ... gives the whole number remainder, "how many things didn't fit since the last even division?"
# // # floor division is that
# <
# >
# <=
# >=
# += # x = x + 1 --> x += 1
# -=
# ** # raise to a power ... x**y --> pow(x,y), math.pow(x,y)
# != # Not equal
# # keywords
# in  # membership check... if myStr in myList;
# not # if not myStr in myList:
# and
# or # any one True will make true.

# Comp 2
# Control Flow... how and when you do what
# IF statements... if, if/else, if/elif if/elif/else

#  LOOPS
# WHILE - a general purpose loop, an IF that repeats
# FOR - repeating action for every item in a container, or a known number of times... range()

# for ___ in _someContainer_:
# for item in myList:
# for char in myStr: used for String
myStr = "IF statements"
for char in myStr:
    print(char)


# for key in myDict: # with dict loop var holds the key... myDic[key]

# membership check on a dict
# if myStr in myDict: # checking the keys
#     if myStr in myDict{value}

# for num in range(5): # for  ___ in range(0, 5, 1)

# if I want the index as I'm looping
# 2 options... range() of len(), or enumerate()
# for i in range(len(myList)):
# for i, item in enumerate(myList):
#
# if I want the index( directly, no in a loop)
# myList.index(myStr) # return the index, or raise an error


#  FILL THE BASKET, accumulator, filter
# firstContainer = ['this thing', 'another', 'an another']
# newContainer = []
# for item in firstContainer:
#     if __
#         newContainer.append(item)

# FUNCTIONS

# modula .. a function has ONE specific job.
# defining/writing a function vs calling it.
# print/output or return(or maybe something else)
# none in your output in a function means it is not return anything.
# parameters are special variables for holding stuff coming into the function
# parameters vs arguments

# This is for chapter 7 structure.
# def someFunction(x, y):
#     return (x + y) * 2 * (x - 1)


# see "task" in the last section of Ch 10, 11, 13, 14 for function writing practice
# CodingBat also has good function -base Python questions
# https://codingbat.com/python
# if __name__ == "__main__":
    # input1 = int(input())
    # input2 = int(input())

    # print(someFunction(input1, input2))


# Built-In Functions
# print()
# input()
# len()
# range()
# sum()
# chr() #ASCII to value
# ord() # number to ASCII
# list()
# int()
# float()
# dict()
# pow() #
# abs() # compare to math.fabs()
# enumerate()
# round() # compare to math.ceil(), math.floor()
# type()
# help(str)
# print(dir(str))
# help(str, isspace), help("if")
# print(dir(str))