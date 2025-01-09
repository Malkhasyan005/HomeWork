def custom_map(func, iterable):
    res = []
    if func is None:
        return res
    for el in iterable:
        res.append(func(el))
    return res

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
result = custom_map(square, numbers)
print(result) 