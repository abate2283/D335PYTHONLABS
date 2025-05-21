# 🔁 Problem 1: Parse Dates with Abbreviated Month Names
#
# Prompt:
#
# Write a program that reads dates in the format Mar 1, 1990
# and converts them to the format 3/1/1990.
# Ignore any date not in the correct format. Input ends with -1.
#
# Example Input:
#
# Mar 1, 1990
# Feb 20 1995
# Jun 12, 2003
# 7/20/2010
# -1
#
# Expected Output:
#
# 3/1/1990
# 6/12/2003

def get_month_as_int(monthString):
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0
    return month_int


if __name__ == "__main__":
    prompt = "Please enter a date: "
    while True:
        dateEntry = input(prompt)
        if dateEntry == "-1":
            break
        parts = dateEntry.split()
        print(parts)
        if len(parts) == 3 and parts[1].endswith(","):
            month_string = parts[0]
            day_string = parts[1].replace(",", "")
            year_string = parts[2]

            month_int = get_month_as_int(month_string)
            print(month_int)
            if month_int != 0:
                print(f"{month_int}/{int(day_string)}/{int(year_string)}")

    # input = Feb 20 1995
    # output = 3 / 1 / 1990
    # Mar 1, 1990
    # Feb 20 1995
    # Jun 12, 2003
    # 7/20/2010
    # -1

















#
# 📅 Problem 4: Extract Year from Date Strings
#
# Prompt:
#
# Write a program that reads dates in the format Month Day, Year. Print just the year for each valid date. Stop on -1.
#
# Example Input:
#
# January 2, 2001
# Feb 4 1999
# March 3, 2010
# -1
#
# Expected Output:
#
# 2001
# 2010
#
# 🆔 Problem 5: Filter User IDs
#
# Prompt:
#
# Write a program that reads user IDs until -1. Print only those that are exactly 8 characters long and start with an uppercase letter.
#
# Example Input:
#
# JohnDoe1
# Jane2022
# ALPHA123
# bobby456
# -1
#
# Expected Output:
#
# ALPHA123
#
