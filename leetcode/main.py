#ls = [1,2,5,8,11,47,89,125,547,1000]
#target = 1000000
#
#l = 0
#r = len(ls) - 1
#
#while l <= r:
#    mid = (l + r) // 2
#    #print(mid)
#    if ls[mid] == target:
#        #print("ind",mid)
#        break
#    elif ls[mid] > target:
#        r = mid - 1
#    elif ls[mid] < target:
#        l = mid + 1
#
#
#def binary_search(ls, taregt, l, r):
#    mid = (l + r) // 2
#    if l > r:
#        return -1
#    if ls[mid] == target:
#        return mid
#    if ls[mid] > target:
#        return binary_search(ls, target, l, mid - 1)
#    if ls[mid] < target:
#        return binary_search(ls, target, mid + 1, r)
#
#
#if binary_search(ls, target, l, r) < 0:
#    print('hello')

#def maxel(ls):
#    if len(ls) == 1:
#        return ls[0]
#    return ls[0] if ls[0] > maxel(ls[1:]) else maxel(ls[1:])
#
#print(maxel([1,9,4,2,3,5,8])





#nums = [1,2,3]
#ans = [[]]
#for num in nums:
#    cur_ans = ans.copy()
#    for el in cur_ans:
#        ans.append(el + [num])
#   
#
#
#print(ans)




st = input()

st2 = ""

lett = "aoyeui"

for let in st:
    let = let.lower()
    if let not in lett:
        st2 += '.' + let
    
print(st2)














