def range_generator(start, stop, step=1):
    while start <= stop:
        yield start
        start += step

gen = range_generator(1, 10, 2)
for num in gen:
    print(num)