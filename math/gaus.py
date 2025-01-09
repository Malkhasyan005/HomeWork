mx = [[1, 2, -1, 0, 2],
      [0, 1, 1, -2, -3],
      [2, 4, 1, -3, -2],
      [1, -4, -7, -1, -19]]

mx2 = [[1,-5,-8,1,3],
       [3,1,-3,-5,1],
       [1,0,-7,2,-5],
       [0,11,20,-9,-2]]

def gaus(mx):
    for j in range(len(mx) - 1):
        for i in range(j + 1, len(mx)):
            num = (mx[i][j] / mx[j][j])
            if (mx[i][j] > 0 and mx[j][j] * num < 0) or (mx[i][j] < 0 and mx[j][j] * num > 0):
                for k in range(len(mx[i])):
                    mx[i][k] += mx[j][k] * num
            else:
                for k in range(len(mx[i])):
                    mx[i][k] -= mx[j][k] * num

    return mx

g = gaus(mx2)
for i in g:
    print(i)
