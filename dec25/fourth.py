def custom_reduce(func, iterable):
    res = iterable[0]
    if func is None:
        return -1
    for el in iterable[1:]:
        res = func(res, el)
    return res

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
result = custom_reduce(add, numbers)
print(result)