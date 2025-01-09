def sum_of_digits(num):
    cnt = 0
    for n in str(num):
        cnt += int(n)
    return cnt

print(sum_of_digits(123))
