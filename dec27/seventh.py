def cumulative_sum(nums):
    sum = 0
    for num in nums:
        sum += num
        yield sum

numbers_list = [1, 3, 5, 2]
for partial_sum in cumulative_sum(numbers_list):
    print(partial_sum)