items = [2, 3, 5, 2, 8, 5, 6, 3]
cnt_dict = {}

for num in items:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

for num, cnt in cnt_dict.items():
    if cnt == 1:
        print(num, end=' ')
