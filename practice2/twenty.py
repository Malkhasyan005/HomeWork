mx = [[1,2,3],
      [4,5,6],
      [7,8,9]
      ]

cnt = 0
ln = len(mx)

for i in range(ln):
    for j in range(i + 1, ln):
        cnt += mx[i][j]

print(cnt)
