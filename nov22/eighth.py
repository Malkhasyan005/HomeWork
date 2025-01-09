#text = ""
#
#with open("source.txt", 'r') as f:
#    text = f.read()
#
#with open("destination.txt", "w") as f:
#    f.write(text)

with open("source.txt", 'r') as f:
    with open("destination.txt", "w") as f1:
        f1.write(f.read())
