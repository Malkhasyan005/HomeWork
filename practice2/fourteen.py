mx = [[9,8,3],
      [6,4,1],
      [7,2,5]
      ]

mn = mx[0][0]
mnind = ()

for i in range(len(mx)):
    for j in range(len(mx[i])):
        if mx[i][j] < mn:
            mn = mx[i][j]
            mnind = (i + 1, j + 1)

print(mnind)
