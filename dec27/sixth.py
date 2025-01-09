def even_numbers(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

numbers_list = [1, 2, 3, 4, 5, 10, 11, 14]
for even in even_numbers(numbers_list):
    print(even)