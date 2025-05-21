x = int(input("Please enter a number which is not 0: "))

total = 1
i = 0

while i < x:
    total = total * x
    print("\nDEBUG: i is ")
    print("Put i to output", i)
    print("\nDEBUG: total is ")
    print("Put total to output", total)
    i = i + 1
