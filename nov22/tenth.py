with open("img.jpg", 'rb') as fs:
    with open("copy_img.jpg", 'wb') as fs1:
        fs1.write(fs.read())
