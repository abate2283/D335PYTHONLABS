# Finding the maximum even number in a list by iterating over every element.

nums = [1, 4, 15, 456]

max_even = None
for num in range(len(nums)):
    index = nums[num]
    print(f'{num}: {index}')
    if num % 2 == 0:  # The number is even?
        if max_even == None or num > max_even:  # Greatest even number seen?
            max_even = num
