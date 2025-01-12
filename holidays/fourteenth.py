def custom_filter_with_yield(func, iterable):
    if func is None:
        func = bool

    for el in iterable:
        if func(el):
            yield el

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = custom_filter_with_yield(is_even, numbers)
for el in result:
    print(el)