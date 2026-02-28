numbers = [1, 2, 3]
it = iter(numbers)  
print(next(it)) 
print(next(it)) 
print(next(it))


text = "Hello World!"
it = iter(text)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


letters = ['a', 'b', 'c']
it = iter(letters)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


my_dict = {'x': 1, 'y': 2}
it = iter(my_dict)
for key in it:
    print(key, my_dict[key])


def gen_numbers():
    yield 1
    yield 2
    yield 3
for n in gen_numbers():
    print(n)


def gen_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
print(list(gen_even(10)))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(6)))