mx = [[1,  2,  3,  4],
      [5,  6,  7,  8],
      [9,  10, 11, 12],
      [13, 14, 15, 16]]

#mx = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

ln = len(mx)
mx2 = []

for i in range(ln - 1, -1, -1):
    ls = []
    for j in range(ln - 1, -1, -1):
        ls.append(mx[i][j])
    mx2.append(ls)
print(mx2)


#--------------------------------------------------------------------------------------

n = ln - 1
for i in range(ln):
    for j in range(i, ln):
        if i != j or i + j <= ln // 2:
            mx[i][j], mx[n - i][n - j] = mx[n - i][n - j], mx[i][j]

print(mx)
