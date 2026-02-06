for q in range(6):
  print(q)
for w in range(1, 6):
    print(w)
for e in range(2, 11, 2):
    print(e)
for r in range(5, 0, -1):
    print(r)
for t in range(1, 6):
    print(t * t)


for a in range(1, 6):
    if a == 4:
        break
    print(a)
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num == 7:
        break
    print(num)
for s in range(1, 100):
    print(s)
    if s == 5:
        break
total = 0
for d in range(1, 10):
    total += d
    if total > 10:
        break
    print(total)
numb = [4, 6, 2, -1, 9]
for nums in numb:
    if nums < 0:
        break
    print(nums)


for z in range(1, 6):
    if z == 3:
        continue
    print(z)
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
nu = [2, -3, 5, -1, 4]
for n in nu:
    if n < 0:
        continue
    print(n)
for c in range(1, 11):
    if c % 3 == 0:
        continue
    print(c)


sizes = ["small", "medium", "large"]
shirts = ["t-shirt", "sweater", "jacket"]

for size in sizes:
    for shirt in shirts:
        print(size, shirt)

colors = ["red", "blue", "black"]
cars = ["sedan", "suv", "truck"]

for color in colors:
    for car in cars:
        print(color, car)

teachers = ["Mr. Smith", "Ms. Lee"]
subjects = ["Math", "Science", "English"]

for teacher in teachers:
    for subject in subjects:
        print(teacher, subject)

animals = ["dog", "cat"]
actions = ["runs", "sleeps", "jumps"]

for animal in animals:
    for action in actions:
        print(animal, action)

countries = ["USA", "France"]
cities = ["New York", "Paris", "Lyon"]

for country in countries:
    for city in cities:
        print(country, city)
