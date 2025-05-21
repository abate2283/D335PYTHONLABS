imax = -1
# input: 22 5 99 3 0
entry = int(input("Get next value: "))
while entry != 0:
    if entry > imax:
        imax = entry
    entry = int(input("Get next value: "))

print(f"imax: {imax}")

# finding minimum

# imin = 0
# val = int(input("Get next value: "))
# while val != 0:
#     if (val < imin) and (val > 0):
#         imin = val
#     val = int(input("Get next value: "))
# print(f"imin is: {imin}")
