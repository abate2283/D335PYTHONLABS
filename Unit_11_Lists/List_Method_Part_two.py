# numberList = list(range(10))
# wordList = list("Thequickbrownfox")
# print(wordList.sort())
# getIndex = numberList.count(2)
# print(getIndex)

text = 'Jan Sam Ann Joe Tod'
user_input = input()
short_names = user_input.split()
print(short_names)
###Remember that sort() and reverse() don't return any value so you have to print the original variable!!!!!
short_names.sort()
short_names.reverse()
print(short_names)



#
# # Original string
# # text = 'Jan Sam Ann Joe Tod'
# user_input = input()
# # Split the string into a list of words
# words = user_input.split()
#
# # Sort the list of words
# words.sort()
# words.reverse()
#
# # Join the sorted list back into a string
# sorted_text = ' '.join(words)
#
# print(sorted_text)


