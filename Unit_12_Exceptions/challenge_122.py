numbers = [2, 4, 5, 8]
prompt = "Enter a value:\n"
user_input = input(prompt)
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor > 20:
            # Possible NameError
            # compute() is not defined
            result = compute(result)
        elif divisor < 0:
            # Possible IndexError
            result = numbers[divisor]
        else:
            # Possible ZeroDivisionError
            result = 20 // divisor          # // truncates to an integer
        print(result, end=' ')
    except (ValueError, ZeroDivisionError):
        print('r', end=' ')
    except (NameError, IndexError):
        print('s', end=' ')
    user_input = input(prompt)
print('OK')