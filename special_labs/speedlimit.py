# speed_limit = int(input("Enter speed limit: "))
# driving_speed = int(input("Enter driving speed: "))
# speedRange = 0
# if driving_speed - 10 < speed_limit:
#     print(50)

user_text = input("Please enter a phrase: ")

if "," in user_text:
    user_text = user_text.replace(",", "")

    if "." in user_text:
        user_text = user_text.replace(".", "")

        if " " in user_text:
            user_text = user_text.replace(" ", "")
            if "!" in user_text:
                user_text = user_text.replace("!", "")


print(len(user_text))

