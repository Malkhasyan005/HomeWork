def custom_enumerate(iterable, start = 0):
    return [(i, iterable[i - start]) for i in range(start, len(iterable) + start)]

fruits = ['apple', 'banana', 'cherry']
result = custom_enumerate(fruits, start = 15)
print(result)