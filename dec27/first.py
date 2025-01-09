def simple_sequence(start, end):
    if start > end:
        yield
    while start <= end:
        yield start
        start += 1

gen = simple_sequence(1, 5)
for num in gen:
    print(num, end=' ')

print()