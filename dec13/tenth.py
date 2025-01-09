import os

def search_word1(directory, word):
    ###
    if not os.path.isdir(directory):
        return
    ###
    res = 0
    direct = [di for di in os.listdir(directory) if os.path.isdir(os.path.join(directory, di))]
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    
    for file in files:
        with open(directory + '/' + file, 'r') as fs:
            #print(fs.read())
            #fs.seek(0)
            text = fs.read()
            res += text.count(word)
            #print(res)

    for di in direct:
        res += search_word1(directory + '/' + di, word)
        #print(res)

    return res


def search_word2(directory, word):
    ###
    if not os.path.isdir(directory):
        return
    ###
    res = 0
    files = os.listdir(directory)

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            with open(directory + '/' + file, 'r') as fs:
                text = fs.read()
                res += text.count(word)
                #print(res)
        elif os.path.isdir(os.path.join(directory, file)):
            res += search_word2(directory + '/' + file, word)

    return res

print(search_word1('example', "15"))
print(search_word2('example', "15"))
