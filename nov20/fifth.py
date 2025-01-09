ls1 = [1,3,5]
ls2 = [2,4,6]

it1 = iter(ls1)
it2 = iter(ls2)

while True:
    try:
        print(next(it1))
        print(next(it2))
    except StopIteration:
        break
