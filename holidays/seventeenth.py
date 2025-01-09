def multy_func(multiplayer):

    def multiply(num):

        return num * multiplayer
    
    return multiply

multiply_by_2 = multy_func(2)
multiply_by_3 = multy_func(3)

print(multiply_by_2(5))
print(multiply_by_3(5))