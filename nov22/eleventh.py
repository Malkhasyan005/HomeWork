logs = {"INFO" : 0, "WARNING" : 0, "ERROR" : 0}

with open("log.txt", 'r') as fs:
    for line in fs.readlines():
        if line.startswith("INFO"):
            logs["INFO"] += 1
        elif line.startswith("WARNING"):
            logs["WARNING"] += 1
        elif line.startswith("ERROR"):
            logs["ERROR"] += 1

for key, value in logs.items():
    print(f"{key}: {value}")
