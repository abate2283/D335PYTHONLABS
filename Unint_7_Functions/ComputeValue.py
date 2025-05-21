def compute(numbers):
    result = 0
    for num in numbers:
        try:
        # result -= num * 2
            result = result - (num *2)
            if result < 0:
                raise ValueError("Wrong Value")
        except ValueError as e:
            print("Error", e)
    return result

values = [5, 4, 6]
computed_value = compute(values)
print(computed_value)