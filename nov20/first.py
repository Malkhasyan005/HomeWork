ls = [1,2,3,4,5]
it = iter(ls)

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        break
