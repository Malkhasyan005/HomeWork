# Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both 3 and 5, print "FizzBuzz". Additionally, for numbers that are prime, print "Prime" instead of the number.

#prime_st = {2}
#
#for i in range(3, 101):
#    for j in range(2, i // 2 + 1):
#        if i % j == 0:
#            break
#    else:
#        prime_st.add(i)
#
#for i in range(1, 101):
#    if i % 3 == 0 and i % 5 == 0:
#        print(f"{i} is FizzBuzz")
#    elif i % 5 == 0:
#        print(f"{i} is Buzz")
#    elif i % 3 == 0:
#        print(f"{i} is Fizz")
#    else:
#        print(i)
#
#    if i in prime_st:
#        print(f"{i} is Prime")

# Create a program that asks the user to enter a password and checks for the following criteria using nested ifs: 

pasw = input("Enter a Password: ")
mydict = {
        "UpperCase": False,
        "LowerCase": False,
        "Number": False,
        "Character": False
        }

chars = "!@#$%^&*"

for char in pasw:
    if 48 <= ord(char) <= 57:
        mydict["Number"] = True
    elif 65 <= ord(char) <= 90:
        mydict["UpperCase"] = True
    elif 97 <= ord(char) <= 122:
        mydict["LowerCase"] = True
    elif char in chars:
        mydict["Character"] = True

if len(pasw) < 8:
    print("Password must be at least 8 charachter long")

for key, value in mydict.items():
    if value == False:
        print(f"Pasword must include {key}") 


# Given two 3x3 matrices represented as nested lists, use nested loops to compute and display their product.

#matrix = [
#        [1, 5, 6],
#        [8, 4, 2],
#        [9, 7, 3]
#        ]
#res = 1
#
#for row in matrix:
#    for el in row:
#        res *= el
#
#print(f"Result = {res}")

# Given two variables a and b, swap their values using tuple unpacking and without using a temporary variable.

#a = input("Enter first variable: ")
#b = input("Enter second variable: ")
#print(f"a = {a}, b = {b}")
#
#a, b = b, a
#print(f"a = {a}, b = {b}")

# Given two lists keys = ['name', 'age', 'city'] and values = ['Alice', 30, 'New York'], use a loop to create a dictionary by assigning elements from keys to corresponding elements in values.

#keys = ['name', 'age', 'city']
#values = ['Alice', 30, 'New York']
#mydict = {}
#
#for i in range(len(keys)):
#    mydict[keys[i]] = values[i]
#
#print(mydict)











































