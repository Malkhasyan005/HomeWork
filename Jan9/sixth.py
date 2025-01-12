def memoize(fn):
    chach = {}
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        # print(key)
        if chach.get(key):
            return chach[key]
        res = fn(*args, **kwargs)
        chach[key] = res
        return res
    return inner

@memoize 
def fibonacci(n, memory = {}):
    if n <= 1: 
       return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
print(fibonacci(8))
print(fibonacci(5))
# print(fibonacci(10))
print(fibonacci(12))

