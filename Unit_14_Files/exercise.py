# numInput = int(input("Get value: "))
#
# numList = []
# count = 1
# while numInput != -1:
#     numList.append(numInput)
#     if numInput in numList:
#         count += 1
#         numInput = int(input("Get value: "))


d = {"name": ["hw1", "hw2", "midterm", "final"],
     "Petr Little": [9, 8, 85, 78],
     "Sam Tarley": [10, 10, 99, 100],
     "Joff King": [4, 2, 55, 61]}

print(sorted(d))