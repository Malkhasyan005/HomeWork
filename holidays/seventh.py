def reverse_string(st):
    res = ""
    for i in range(len(st)):
        res += st[len(st) - 1 - i]
    return res

print(reverse_string("hello"))