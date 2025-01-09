def custom_filter(func, iterable):
    res = []
    if func is None:
        for el in iterable:
            if el:
                res.append(el)
        return res
    for el in iterable:
        if func(el):
            res.append(el)
    return res

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = custom_filter(is_even, numbers)
print(result) 
