team = ["quarter back", "wide receiver", "tight end", "kicker"]
user_entry = input("Please enter football player's position: ")
if user_entry in team:
    print(user_entry, "is found in team.")
else:
    print("Invalid")

if user_entry not in team:
    print(f"{user_entry} not found in team.")
else:
    print(f"{user_entry} found in team.")