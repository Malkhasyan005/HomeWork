from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(1), is_prime(5), is_prime(6), is_prime(9), is_prime(2))
