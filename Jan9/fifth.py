def repeat(n):
    def decorator(fn):
        def inner(*args, **kwargs):
            for i in range(n):
                fn(*args, **kwargs)
        return inner
    return decorator

@repeat(4) 
def greet(): 
    print("Hello!")

greet()
