from collections import namedtuple

Player = namedtuple("Player", ['name', 'number', 'position', 'team'])
football = Player("Lamar Jackson", 8, 'quarter back', 'Baltimore Ravens')
# print(football.name, 'the', football.position, 'with jersey #', football.number, 'of the', football.team)
print(f"{football.name}, the {football.position} with jersey # {football.number} of the {football.team} ")

prices = ["$25", 2, 7]
user = int(input("enter a value: "))
if user in prices:
    print(f"{user} is in prices")
else:
    print("user not found")