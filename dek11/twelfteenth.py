def reverse_string(s):
    n = len(s)
    res = ""
    for i in range(n):
        res += s[n - i - 1]
    return res

print(reverse_string("Hello"))
