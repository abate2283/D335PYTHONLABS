# CHALLENGE ACTIVITY
# 5.9.1: Membership and Identity: Enter the output of the code. PAY ATTENTION
x = 2
y = 456
if x is y:
    print("They are the same.")
elif id(x) == id(y):
    print("Same as well")
# else:
#     print("Not same.")
if x is not y:
    print("x and y are not bound to same object.")

w = 500
x = 500 + 500  # Create a new object with value 1000
y = w + w      # Create a second object with value 1000
z = x          # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('z and y are NOT bound to the same object')