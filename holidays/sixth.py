def calculate_average(*args):
    res = 0
    for i in args:
        res += i
    return res / len(args)

print(calculate_average(1,2,3,4,5,6))