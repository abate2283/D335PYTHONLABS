# 📅 Problem 4: Extract Year from Date Strings
#
# Prompt:
#
# Write a program that reads dates in the format Month Day, Year.
# Print just the year for each valid date. Stop on -1.
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

try:
    prompt = "Enter a valid date: "
    while True:
        date_entry = input(prompt).strip()
        if date_entry == "-1":
            break
        if date_entry.count(",") == 1:
            token = date_entry.split()
            if len(token[-1]) == 4 and token[-1].isdigit():
                print(int(token[-1]))

except ValueError as e:
    print(e)