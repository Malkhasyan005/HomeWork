def zip_generator(*iterable):
    iters = [iter(it) for it in iterable]
    while True:
        try:
            yield tuple(next(iter) for iter in iters)
        except (StopIteration, RuntimeError):
            break

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
result = zip_generator(list1, list2)
for el in result:
    print(el)