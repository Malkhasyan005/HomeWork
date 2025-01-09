def order_item(item, quantity = 1, *args, **kwargs):
    print(item)
    print(quantity)
    for el in args:
        print(el, end = " ")
    print()
    for key, value in kwargs.items():
        print(f"{key} = {value}")

order_item("Bob", 15, "one", "two", "three", name="Alice", age=22, city="Paris")

