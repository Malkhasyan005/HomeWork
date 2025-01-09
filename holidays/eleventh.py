def custom_enumerate(iterable, start=0):
    ind = start
    for item in iterable:
        yield ind, item
        ind += 1

ls = ['a', 'b', 'c', 'd']

enumer = custom_enumerate(ls)

for i in enumer:
    print(i)