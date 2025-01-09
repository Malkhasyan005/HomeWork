numbers = list(range(1, 11))

squares_list = [x ** 2 for x in numbers]

squares_gen = (x ** 2 for x in numbers)

print("List:", squares_list)
print("Gen object:", squares_gen)

for sq in squares_gen:
    print(sq)