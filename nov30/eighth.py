x = 15

print("Global x:",x)

def modify_variable():
    global x;
    x = "hello"
    print("Local x:",x)

modify_variable()
print("Global x:",x)
