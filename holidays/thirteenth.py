def custom_map_with_yield(func, *iterables):
    iters = [iter(it) for it in iterables]
    while True:
        try:
            values = [next(iter) for iter in iters]
            print(values)
            yield func(*values)
        except StopIteration:
            break

def square(x, y):
    return y ** x

gen = custom_map_with_yield(square, [1,2,3,4,5,6], [11,21,31,14,15,61,71])

for el in gen:
    print(el)