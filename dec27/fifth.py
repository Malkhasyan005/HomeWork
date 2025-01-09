def fibonacci(limit=None):
    a = 0
    b = 1
    while limit is None or a < limit:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))

for num in fibonacci(limit=100):
    print(num)