vowel = {'ա', 'ե', 'ը', 'ի', 'ո', 'ու'}
words = ['անուն', 'գիրք', 'խնձոր', 'մեքենա', 'տուն']

for word in words:
    cnt = 0
    for let in word:
        if let in vowel:
            cnt += 1
    print(f"{word} has {cnt} vowel letter")
