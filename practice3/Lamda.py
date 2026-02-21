def multiply(x, y):
    return x * y

multiply_lambda = lambda x, y: x * y

print(multiply(3, 4))       
print(multiply_lambda(3, 4))


celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)



students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90)
]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)



def calculate_discount(price):
    if price > 100:
        return price * 0.9
    else:
        return price

discount = lambda price: price * 0.9 if price > 100 else price

print(calculate_discount(150))  
print(discount(150))

