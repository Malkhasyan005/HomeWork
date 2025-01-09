def factorial(n):
    res = 1
    for i in range(1,n + 1):
        res *= i
    return res

print(factorial(1), factorial(5), factorial(3))
