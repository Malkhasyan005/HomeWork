mx = [[3,2,-1],
      [2,-1,4],
      [5,1,2]]


def determinant(mx):
    if len(mx) == 1:
        return mx[0]
    if len(mx) == 2:
        return mx[0][0] * mx[1][1] - mx[0][1] * mx[1][0]

    det = 0
    for i in range(len(mx)):
        submx = []
        for k in range(1, len(mx)):
            row = []
            for j in range(len(mx)):
                if j != i:
                    row.append(mx[k][j])
            submx.append(row)
        det += pow(-1, i) * mx[0][i] * determinant(submx)

    return det


print(determinant(mx))


########################

#MCA

########################

def foo(x, arr = []):
    arr.append(x)
    print(arr)


foo(8)
foo(7)
ls = [2]
foo(10, ls)
foo(10)
foo(20,ls)
