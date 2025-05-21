N = float(input())  # Read user-entered number
total = N
# Initialize the loop variable
i = total - 1

while i >= 1:
    total *= i
    # Set total to total * (i)
    # Decrement i
    i -= 1

print(f"{N}:{total:.2f}")


n = 1
while n < 3:
    print(n - 2)
    n = n + 1


