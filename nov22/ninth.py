with open("data.txt", 'r') as f:
    with open("cleand_data.txt", 'w') as f1:
        for line in f.readlines():
            if line.strip() != "":
                f1.write(line)
