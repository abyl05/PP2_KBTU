def greet(name):
    """
    This function takes a person's name as input
    and returns a greeting message.
    """
    return "Hello, " + name + "!"

# Calling the function
message = greet("Alice")
print(message)


def power(base, exponent=2):
    """
    Returns the value of base raised to the given exponent.
    If exponent is not provided, it defaults to 2.
    """
    return base ** exponent

# Calling with both arguments
print(power(3, 3))  # 27

# Calling with one argument (uses default exponent=2)
print(power(4))


def add_numbers(*args):
    """
    Accepts any number of numeric arguments
    and returns their sum.
    """
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3, 4))


def display_info(**kwargs):
    """
    Accepts any number of keyword arguments
    and prints them as key-value pairs.
    """
    for key, value in kwargs.items():
        print(key + ":", value)

display_info(name="John", age=25, city="New York")


def find_max(numbers):
    """
    Takes a list of numbers as input
    and returns the largest number.
    """
    max_value = numbers[0]  # Assume first number is largest initially
    
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

# List to pass into function
my_list = [10, 45, 23, 67, 12]

print(find_max(my_list))


def add_item(item_list, item):
    """
    Adds an item to the given list.
    Demonstrates that lists are mutable (can be changed).
    """
    item_list.append(item)

shopping_list = ["milk", "bread"]

add_item(shopping_list, "eggs")

print(shopping_list)