# result = 0

# for n in range(6):
#     result = n - 2
#
#     if (result % 2) != 0:
#         print('_', end=' ')
#         continue
#
#     print(result, end=' ')
#
# print('done')

# stop = int(input())
#
# for a in range(4):
#     result = 0
#
#     for b in range(3):
#         result += a * b
#
#     print(result)
#
#     if result > stop:
#         break

stop = int(input("Enter a number: "))
result = 0

for a in range(5):
    print(a + 1, end=': ')

    for b in range(3):
        result += a + 1

        if result > stop:
            print('_', end=' ')
            continue

        print(result, end=' ')

    print()