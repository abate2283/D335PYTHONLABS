# 🔢 Problem 3: Format Phone Numbers
#
# Prompt:
#
# Read input lines in the format 123-456-7890.
# Validate and reformat each valid number to (123) 456-7890.
# Ignore invalid ones. Stop at -1.
#
# Example Input:
#
# 123-456-7890
# 9876543210
# 111-222-3333
# -1
#
# Expected Output:
#
# (123) 456-7890
# (111) 222-3333

try:
    prompt = "Enter number: "
    while True:
        number = input(prompt).strip()
        if number == "-1":
            break
        if number.count("-") == 2:
            part = number.split("-")
            if len(part) == 3:
                area_code = part[0]
                middle_code = part[1]
                last_four = part[2]
                if (area_code.isdigit() and len(area_code) == 3
                and middle_code.isdigit() and len(middle_code) == 3
                and last_four.isdigit() and len(last_four) == 4):
                    print(f"({area_code}) {middle_code}-{last_four}")
except ValueError as e:
    print(e)