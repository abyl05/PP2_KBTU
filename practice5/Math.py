import math

numbers = [5, 10, 2, 8]
print("Min:", min(numbers))
print("Max:", max(numbers))


print(abs(-7)) 
print(abs(3.5))


print(round(3.14159, 2))
print(pow(2, 3))


print(math.sqrt(16))
print(math.pow(2, 5))


print(math.ceil(3.2))
print(math.floor(3.8)) 


print(math.sin(math.pi/2))
print(math.cos(0))         
print(math.e)

import random

print(random.random())
print(random.randint(1, 10))


colors = ["red", "blue", "green"]
print(random.choice(colors))


cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)