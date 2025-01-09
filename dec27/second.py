def countdown(n):
    while n:
        print(f"Yielding {n}")
        yield n
        n -= 1

gen = countdown(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
