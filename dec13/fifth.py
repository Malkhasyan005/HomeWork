def reverse_string(s):
    res = ""
    for i in range(len(s)):
        res += s[len(s) - 1 - i]
    return res

print(reverse_string("hello"))
