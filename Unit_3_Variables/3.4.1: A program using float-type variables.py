import math

miles = float(input('Enter the miles you want to calculate: '))
hours_to_drive = miles/60.00
hours_to_fly = miles/500.00

print(miles, 'mile is equals to:')
print(hours_to_fly, 'Hours to fly.')
print(f'{hours_to_drive:.4f}')
print(f'{math.pi:.4f}')
