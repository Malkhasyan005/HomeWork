def counter():
    count = 0
    
    def inner_counter():
        nonlocal count;
        count += 1
        print(f"Function has called {count} times")

    return inner_counter

my_counter = counter()

my_counter()
my_counter()
my_counter()