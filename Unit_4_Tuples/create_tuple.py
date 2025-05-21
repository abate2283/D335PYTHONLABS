# nums = (5, 15, 20)
# num_set = set(nums)
# myList = []
# myList.extend(num_set)
# print(myList)
#
# string = "names"
# print(string.index("n"))

# n = int(input("Please enter 25: "))
#
# for i in range(n):
#     if i % 2 == 0:
#
#         print(i//2)
#     elif i % 2 == 1:
#         print(f"{i//2} \t {3*i + 1}")
#

# tictac = ['tic', 'tac', 'toe']
# for i, v in enumerate(tictac):
#     print(v, end=" ")

books = []
prompt = 'Enter new book: '
user_input = input(prompt).strip()

while (user_input.lower() != 'exit'):
    books.append(user_input)
    user_input = input(prompt).strip()

books.sort()

print('\nAlphabetical order:')
for book in books:
    print(book)
