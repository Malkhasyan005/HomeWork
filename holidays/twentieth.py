def string_expender():
    st = ''

    def add_to_string(str):
        nonlocal st
        try:
            st += str
        except:
            print("Something went wrong!!")
        return st
    
    return add_to_string

st_ex = string_expender()

print(st_ex("Hello"))
print(st_ex(" World"))


print(st_ex(15))


print(st_ex("New String")) 