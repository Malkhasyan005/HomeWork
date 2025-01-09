def zip_generator(iterable1, iterable2):
    lenght = len(iterable1) if len(iterable1) < len(iterable2) else len(iterable2)
    for i in range(lenght):
        yield (iterable1[i], iterable2[i])

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip_generator(list1, list2)
for el in result:
    print(el)