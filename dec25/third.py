def custom_zip(iterable1, iterable2):
    res = []
    lenght = len(iterable1) if len(iterable1) < len(iterable2) else len(iterable2)
    for i in range(lenght):
        res.append((iterable1[i], iterable2[i]))
    return res

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = custom_zip(list1, list2)
print(result)
