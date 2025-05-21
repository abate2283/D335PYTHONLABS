phrase = 'The Lord is my shepherd I shall not want.'
phrase_list = phrase.split(" ")
# print(phrase_list)
user_input = input("Please enter a word: ")
if user_input in phrase_list:
    print(f"{user_input} means: ")
elif user_input in phrase:
    print(f"{user_input} meaning is: ")
else:
    print(f"{user_input} is invalid.")