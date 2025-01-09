def print_down_from_n(n):
    if n == 1:
        print(n, end = " ")
        return
    print(n, end=" ")
    print_down_from_n(n - 1)
    return

print_down_from_n(10)
