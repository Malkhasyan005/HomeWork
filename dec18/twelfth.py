def flatten_list(ls):
    res = []
    for el in ls:
        #print(el)
        if type(el) == list:
            res += list(flatten_list(el))
        else:
            res.append(el)

    return res


ls = [1, [2, [3, [4]]], 5]
print(flatten_list(ls))