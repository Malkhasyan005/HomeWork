mx = [[1,2,3],
      [4,5,6],
      [7,8,9]
      ]

for i in range(len(mx)):
    for j in range(i, len(mx[i])):
        mx[i][j], mx[j][i] = mx[j][i], mx[i][j]

print(mx)

