def read_file_in_chunks(filepath, chunk_size):
    with open(filepath, 'r') as fs:
        while True:
            text = fs.read(chunk_size)
            if text:
                yield text
            else:
                break

for chunk in read_file_in_chunks("test.txt", 10):
    print(chunk)