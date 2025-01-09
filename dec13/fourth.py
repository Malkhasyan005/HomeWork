def sum_up_to_n(n):
    if n == 1:
        return 1
    return n + sum_up_to_n(n - 1)

print(sum_up_to_n(3))
