mx = [[1,2,3],
      [4,5,6],
      [7,8,9]
      ]
maxel = 0

for i in range(len(mx)):
    for j in range(len(mx[i])):
        if mx[i][j] > maxel:
            maxel = mx[i][j]

print(maxel)

