ls = [1,2,3,4,5]

try:
    print(ls[10])
except IndexError:
    print("Invalid index. Please check the list size.")
