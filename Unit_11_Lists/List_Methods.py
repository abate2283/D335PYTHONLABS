names = list("alfredarreyndipbate")
print(f'Created a new list with the given string {names}')
names.append(list("gilbert"))
# list.append(x)
print(f'Append adds a new list at the end of names: {names}')
# list.extend([x])
names.extend(list("gilbert"))
print(f'Extend merges a new list to the old list: {names}names')
# list.insert(i,n) where i is index an n is value
names.insert(0, "this was inserted in position 0")
print(f'Inserting a value at nth position {names}')
del names[0]
# Deleted index 0;
print(names)
names.remove("d")
print(names)
# names.pop(-1)
names.pop()


# Inserted range in list
list2 = list(range(1000))
for i in list2:
    if i % 20 == 0:
        names.insert(0, list2)
        # print("i % 20 == 0", names)
    elif i % 30 == 2:
        names.insert(9, list2)
        # print("i % 30 == 2", names)
    # else:
    #     # print("Completed")




