input_year = int(input("Please enter a year: "))

is_leap_year = False
if (input_year % 4 == 0) and (input_year % 400 == 0):
    is_leap_year = True
    print(f"{input_year} - leap year")
else:
    is_leap_year = False
    print(f"{input_year} - not a leap year")

