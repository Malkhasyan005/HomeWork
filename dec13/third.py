def print_characters(s):
    if len(s) == 1:
        print(s)
        return
    print(s[0])
    print_characters(s[1:])
    return

print_characters("hello")
