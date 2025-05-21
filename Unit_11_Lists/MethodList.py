my_list = list("xyzabc")
my_list.remove("x")
print(my_list)
my_list.insert(0, "x")
print(my_list)
list.reverse(my_list)
print("reverse List",my_list)
for myVal in my_list:
    print("For Loop:", myVal)