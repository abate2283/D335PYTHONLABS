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
    prompt = "Get values: "
    while True:
        userInput = input(prompt)
        parts = []
        if userInput == "-1":
            parts.append(userInput)
            break
        print(parts)
        if len(parts) == 3 and "," in parts[1]:
            month = parts[0]
            day = parts[1].replace(",", " ")
            year = parts[2]
            month_num = get_month_as_int(month)
            print(f"{month}/{day}/{year}")

# March 1, 1990
# April 2 1995
# 7/15/20
# December 13, 2003
# -1
