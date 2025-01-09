def fib(n):
    ls = [0,1]
    if n == 1:
        return 0
    n -= 2
    for i in range(n):
        ls.append(ls[-1] + ls[-2])

    return ls[-1]

print(fib(7), fib(1), fib(15))
