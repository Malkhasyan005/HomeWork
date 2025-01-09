def custom_map_with_yield(func, iterable):
    for el in iterable:
        yield func(el)

def square(x):
    return x ** 2

gen = custom_map_with_yield(square, [1,2,3,4,5,6])

for el in gen:
    print(el)