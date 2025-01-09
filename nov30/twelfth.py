def filter_positive(ls):
    new_ls = [num for num in ls if num >= 0]
    return new_ls

print(filter_positive([-5, 3, -1, 2, 0]))            
