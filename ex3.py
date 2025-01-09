# 1 Ask the user to enter a string, and then print the string in reverse orderi

#st = input("Enter a text: ")
#revst = st[::-1]
#print(revst)

# 2 Count how many vowels are in the string and print the count.

#st = input("Enter a text: ")
#vowels = ["a","e","i","o","u"]
#cnt = 0
#
#for let in st:
#    if let.lower() in vowels:
#        cnt += 1
#
#print(f"In this word there are {cnt} vowels")

# 3 Write a program that takes a string as input and outputs the longest substring without repeating characters. For example, the string "abcabcbb" should return "abc".

#st = input("Enter a text: ")
#used_letters = {}
#start = 0
#max_lenght = 0
#
#
#for i in range(len(st)):
#    let = st[i]
#
#    if let in used_letters and used_letters[let] >= start:
#        start = used_letters[let] + 1
#
#    used_letters[let] = i
#
#    cur_lenght = i - start + 1
#    if cur_lenght > max_lenght:
#        max_lenght = cur_lenght
#        max_suf = st[start: i + 1]
#
#print(max_suf)

# 4 Write a program using a while loop that repeatedly asks the user to input a number until they input 0, then print the sum of all entered numbers.

#sumnum = 0
#num = int(input("Enter a number: "))
#while num != 0:
#    sumnum += num
#    num = int(input("Enter a number: "))
#
#print(sumnum)

# 5 Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.

mylist = [15, 25, 36, 11, 45, 78, 76, 18, 94, 115]

print(sum(mylist))
