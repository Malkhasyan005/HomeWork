def calculator():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        operation = input("Enter operation(1-5): ")

        if operation == '5':
            print("Exiting calculator...")
            break
        if operation.strip() not in ['1', '2', '3', '4']:
            print("Invalid operation!, enter number between 1-5")
            continue

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
        else:
            print("Invalid input!, enter numbers only")
            continue

        if operation.strip() == '1':
            print(f'{a} + {b} = {a + b}')
        elif operation.strip() == '2':
            print(f'{a} - {b} = {a - b}')
        elif operation.strip() == '3':
            print(f'{a} * {b} = {a * b}')
        elif operation.strip() == '4':
            if b == 0:
                print("Division by zero is not allowed!")
                continue
            print(f'{a} / {b} = {a / b}')


calculator()