import time

def delay(n):
    def decorator(fn):
        def inner(*args, **kwargs):
            print(f"Waiting for {n} seconds...")
            time.sleep(n)
            fn(*args, **kwargs)
        return inner
    return decorator

@delay(2) 
def say_hello(): 
    print("Hello, World!")

say_hello()