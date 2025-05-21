# Task
# 2
#
# Complete
# the
# function
# to
# return the
# last
# X
# number
# of
# characters in the
# given
# string


# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    for i in range(x):
        print(mystring[-i])


# Student code goes here

# expected output: IT
print(getLast('WGU College of IT', 2))

# expected output: College of IT
print(getLast('WGU College of IT', 13))