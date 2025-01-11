def log_execution(fn):
    def inner(*args, **kwargs):
        print(f"Executing {fn.__name__} with arguments {args} and {kwargs}")
        res = fn(*args, **kwargs)
        print(f"{fn.__name__} returned {res}")
    return inner


@log_execution 
def add(a, b):
    return a + b


add(3, 5) 


