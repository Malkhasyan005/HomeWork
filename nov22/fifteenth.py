try:
    with open("exclusive_file.txt", 'x') as fs:
        fs.write("This file is created using x mode.")
except FileExistsError:
    print("File already exist")
