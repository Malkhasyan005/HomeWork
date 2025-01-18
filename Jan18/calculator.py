def calculator():
    while True:
        print("\nBasic Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        answ = int(input("Enter an operation (1-5): "))
        
        if answ == 5:
            print("Exiting. Thank you!!")
            break

        operations = {1: ['+', lambda a,b: a + b],
                      2: ['-', lambda a,b: a - b],
                      3: ['*', lambda a,b: a * b],
                      4: ['/', lambda a,b: a / b]}
        
        if answ not in operations:
            print("Invalid option. Please enter valid operation (1 - 5): ")
        
        else:
            first = input("Enter the first number: ")
            second = input("Enter the second number: ")
            try:
                first = float(first)
                second = float(second)
            except ValueError:
                print("\nInvalid input\nEnter numeric inputs")
                continue
            if int(first) == first: first = int(first)
            if int(second) == second: second = int(second)
            if answ == 4 and second == 0:
                print("ZeroDivisionError!! Enter valid numbers")
                continue
            print(f"{first} {operations[answ][0]} {second} = {operations[answ][1](first, second)}")

calculator()