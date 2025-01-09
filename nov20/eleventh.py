mx = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] 
ls1 = [j for i in mx for j in i]
ls2 = [mx[i][j] for i in range(len(mx)) for j in range(len(mx[i]))]

print(ls1)
print(ls2)
