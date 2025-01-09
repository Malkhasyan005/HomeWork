def find_max(ls):
    if len(ls) == 1:
        return ls[0]
    return max(ls[0], find_max(ls[1:]))

ls = [3, 1, 14, 4, 1, 5]
print(find_max(ls))
