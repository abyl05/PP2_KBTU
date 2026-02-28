def square_generator(n):
    for i in range(n + 1):
        yield i ** 2
        
N = int(input("Enter N: "))
for value in square_generator(N):
    print(value)