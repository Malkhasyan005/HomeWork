def all_greater(arr, target):
    for num in arr:
        if num < target:
            return False
    return True

print(all_greater([5,6,7,8,9,99,45], 10))