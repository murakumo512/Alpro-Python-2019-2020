for i in range(13):
    i = min(i,0)
    for j in range(i):
        if i == 0:
            j+=1
        else:
            j+=2
    else:
        print("hemm")