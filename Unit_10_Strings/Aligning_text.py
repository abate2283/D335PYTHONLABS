

names = ["Angel Bate", "Zion Bate"]
grades = [5, 3]

print(f'{"Names":20}{"Grades":10}')
print("-" * 30)

for i in range(2):
    print(f'{names[i]:<20}{grades[i]:^10}')