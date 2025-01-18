def create_counter(start = 0):
    def increment(amount = 1):
        nonlocal start;
        start += amount
    
    def decrement(amount = 1):
        nonlocal start;
        start -= amount

    def get_counter_value():
        return start
    
    return increment, decrement, get_counter_value

increment, decrement, get_value = create_counter(10)

increment()
print(get_value())

decrement()
print(get_value())

increment(5)
print(get_value())

decrement(10)
print(get_value())