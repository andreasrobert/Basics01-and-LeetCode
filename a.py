def lon(x):

    word = str(x)
    y = ""


    for i in range(len(word)-1, -1, -1):
        if word[i] == "-":
            y = "-" + y
            continue

        y += word[i]
    

    return int(y)
    

    





print(lon(-1234567))