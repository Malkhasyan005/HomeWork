st = "Python"
it = iter(st)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

