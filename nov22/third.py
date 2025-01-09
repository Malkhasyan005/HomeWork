try:
    print(x)
except NameError:
    print("Varable did nor defined.")
    x = input("Plear enter the varable value: ")
    print(x)
