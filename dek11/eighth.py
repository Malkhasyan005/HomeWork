def process_data(data, operation, *args, threshold=None, **kwargs):
    for el in args:
        data.append(el)
    
    res = 0
    
    if kwargs.get("unique", 0) == 1:
        data = set(data)

    if operation == 'sum':
        for el in data:
            res += el

    elif operation == 'multiply':
        res = 1
        for el in data:
            res *= el
    
    elif operation == 'filter':
        if threshold == None:
            return "There are not threshold"
        res = [el for el in data if el > threshold]
        
    if kwargs.get("reverse", 0) == 1:
        try:
            res = res[::-1]
        except:
            res = res
        
    return res


ls = [1,2,3,4,5]
answ1 = process_data(ls, 'sum') # 15
answ2 = process_data(ls, 'multiply') # 120
answ3 = process_data(ls, 'filter', threshold=3) # 4,5
answ4 = process_data(ls, 'sum', 12, 24, 20) # 59
answ5 = process_data(ls, 'multiply', 12, 20, 20, 10, unique=True) # 2400
answ6 = process_data(ls, 'filter', threshold=2, reverse=True) # [5,4,3]

print(answ1, answ2, answ3, answ4, answ5, answ6, sep=' /// ')
