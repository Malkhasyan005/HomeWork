def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(100):
    if is_prime(i):
        print(f'{i} is Prime')
    elif i % 2 == 0:
        print(f'{i} is Even')
    else:
        print(f'{i} is Odd')
