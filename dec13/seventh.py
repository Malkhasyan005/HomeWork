def write_to_file(file_path, **kwargs):
    with open(file_path, 'w') as fs:
        for key, value in kwargs.items():
            fs.write(f"{key} = {value}\n")

write_to_file('python.txt', name = "Karen", age = 20, city = "Gyumri")
write_to_file('example/python.txt', name = "Karen", age = 20, city = "Gyumri")
