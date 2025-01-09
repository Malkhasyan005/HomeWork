ls =["apple", "banana", "cherry"]
it = iter(ls)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("No more items in the iterator.")
        break


