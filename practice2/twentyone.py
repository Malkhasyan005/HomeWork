A = [1, 2, 3, 4, 5]
res = [A]
curls = A

while True:
    newls = []
    for i in range(len(curls) - 1):
        newls.append(curls[i] + curls[i + 1])
    res.append(newls)
    curls = newls
    if len(newls) == 1:
        break

print(res[::-1])
