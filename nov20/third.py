ls = [10,20,30,40]
it = iter(ls)
res = 0

while True:
    try:
        el = next(it)
        res += el
    except StopIteration:
        break

print(res)
