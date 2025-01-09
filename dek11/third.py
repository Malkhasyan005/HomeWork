def sum_numbers(*args):
    res = 0
    for num in args:
        res += num
    return res

answ1 = sum_numbers(1,2,3,4,5)
answ2 = sum_numbers()

print(f"Result1 = {answ1}, Result2 = {answ2}")
