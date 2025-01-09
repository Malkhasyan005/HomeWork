def append_to_file(file_path, *args, **kwargs):
    try:
        with open(file_path, 'a') as fs:
            fs.writelines([st + '\n' for st in args])
            for key, value in kwargs.items():
                fs.write(f"{key} = {value}\n")
    except:
        print("File Not Found")

append_to_file('python2.txt', "Hi everyone", "My name is Jack", "Foo", name = "Jack", age = 15)
append_to_file('example/python2.txt', "Hi everyone", "My name is Jack", "Foo", name = "Jack", age = 15)
