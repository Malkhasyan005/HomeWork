def divide_numbers(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

# print(divide_numbers(1,0))
print(divide_numbers(10,5))