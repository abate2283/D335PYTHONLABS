nestedList = [[0, 1], [2, 3]]
print("Index 0:", nestedList[0])
print("Index 1:", nestedList[1])
print(f"Index of nested: {nestedList[0][0]}")

my_list = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(f"First Index 0: {my_list[0][0]} First Index 1: {my_list[0][1]}")
# print(f"First Index 1: {my_list[0][1]}")
print(f"Second Index 0: {my_list[1][0]}", end=" ")
print(f"Second Index 1: {my_list[1][1]}")
print(f"Third Index 0: {my_list[2][0]}", end=" ")
print(f"Third Index 1: {my_list[2][1]}")

nums = [[10, 20, 30], [98, 99]]
print("nums[0]",nums[0])

scores = [
    [75, 100, 82, 76],
    [85, 98, 89, 99],
    [75, 82, 85, 5]
]
print(f"Score 100: {scores[[0][0][1]]}")
