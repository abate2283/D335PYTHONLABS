prompt = "Get user value:\n"
user_input = int(input(prompt))
while user_input != "q":
    try:
        result = 120/user_input
        print(result)
    except ZeroDivisionError:
        print("Zero Division!!! ")
    except ValueError:
        print("Value Error!!! ")
    except:
        print("x")
    user_input = int(input(prompt))

print("Bye!!!")

# Multiple Exception
# try:
#     # ...
# except (ValueError, TypeError):
#     # Exception handler for any ValueError or TypeError that occurs.
# except (NameError, AttributeError):
#     # A different handler for NameError and AttributeError exceptions.
# except:
#     # A different handler for any other exception type.

# Contruct
# try:
#     # ... Normal code
# except exceptiontype1:
#     # ... Code to handle exceptiontype1
# except exceptiontype2:
#     # ... Code to handle exceptiontype2
# ...
# except:
#     # ... Code to handle other exception types
