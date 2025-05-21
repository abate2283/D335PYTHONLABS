import arithemetic


# Remember that arithmetic.py calculate function might/will have a different definition where it was created:
# Please check that first before solving it here!!!
def calculate(number):
    return number + 4


print(calculate(5))
print(f"second equation: {arithemetic.calculate(5)}")


def one(number):
    return number ** 2


print("OneNumber: ", one(4))
