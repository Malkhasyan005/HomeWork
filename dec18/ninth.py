def binary_search(ls, target, l, r):
    if l > r:
        return -1
    mid = (l + r) // 2
    if ls[mid] == target:
        return mid
    if ls[mid] > target:
        return binary_search(ls, target, l, mid - 1)
    if ls[mid] < target:
        return binary_search(ls, target, l + 1, r)
    

arr = [1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,9]

ind1 = binary_search(arr, 8, 0, len(arr) - 1)
ind2 = binary_search(arr, 1, 0, len(arr) - 1)
ind3 = binary_search(arr, 15, 0, len(arr) - 1)

print(ind1)
print(ind2)
print(ind3)
