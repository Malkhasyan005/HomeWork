def greet_decorator(fn):
    def innit(*args, **kwargs):
        print("Hello!")
        fn(*args, **kwargs)
        print("GoodBye!")
    return innit

@greet_decorator 
def say_name(): 
    print("My name is Python.")

say_name()