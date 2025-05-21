from collections import namedtuple

Car = namedtuple('Car', ['Make', 'Model', 'Price', 'Horsepower', 'Seats'])
suv = Car("Land Rover", "Range Rover", 115000, 5200, 7)
print(suv)
print(f"The description is: {len(suv)}")
print(f'Make is: {suv[0]}')
print(suv[-2])
