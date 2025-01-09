def running_total():
    total = 0

    def add_to_total(num):
        nonlocal total 
        total += num
        return total

    return add_to_total

res = running_total()

print(res(5))
print(res(10))
print(res(3))