from math import sqrt

prime_nums = [x for x in range(2, 101) if all(x % i for i in range(2,int(sqrt(x) + 1)))]

print(prime_nums)