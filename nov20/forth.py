cnt = 3
ls = [2,4,6,8,10]
it = iter(ls)

while cnt:
    try:
        print(next(it))
    except StopIteration:
        break
    cnt -= 1
