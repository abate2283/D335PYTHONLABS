# sum_of_values = 0
# val = int(input("Enter a non negative number: "))
# while val > -1:
#     sum_of_values += val
#     print(sum_of_values)
#     val = int(input("Enter a non negative number: "))

# for i in range(2):
#     print("outer loop", i)
#     for j in range(3):
#         print(j, "inner loop")
# # print(j, "inner loop")

for i in range(5):
    # print("outer", i)
    for j in range(10, 12):
        print(f'{i}{j}')