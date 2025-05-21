# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    for i in range(x):
        print(mystring[i], end="")
    return mystring, x


# Student code goes here

# expected output: WGU
printFirst('WGU College of IT', 3)
print()

# expected output: WGU College
printFirst('WGU College of IT', 11)