filename = input("Enter a filename: ")

try:
    with open(f"{filename}.txt", 'x') as fs:
        fs.write(f"File <{filename}> created successfully.")
except FileExistsError:
    print(f"File with <{filename}> name already exists.")
