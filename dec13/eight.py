def read_from_file(file_path):
    with open(file_path, 'r') as fs:
        data = fs.readlines()
        print(''.join(data))

read_from_file("python.txt")
read_from_file("example/python.txt")

