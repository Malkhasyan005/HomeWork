mx = [[1,2,3],
      [4,5,6],
      [7,8,9]
      ]
ln = len(mx)
cnt = 0

for i in range(ln):
    cnt += mx[i][ln - i - 1]

print(cnt)

