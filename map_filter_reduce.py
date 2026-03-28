from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

print("Original:", nums)

squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)

even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)

total = reduce(lambda x, y: x + y, nums)
print("Sum:", total)

even_nums = list(filter(lambda x: x % 2 == 0, nums))
product = reduce(lambda x, y: x * y, even_nums)
print("Product of even numbers:", product)
