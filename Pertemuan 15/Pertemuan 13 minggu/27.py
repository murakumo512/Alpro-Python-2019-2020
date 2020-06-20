def rekursif(x,y):
    if(y == 0):
        return 1
    else:
        return x * rekursif(x,y-1)


print(rekursif(22,5))

def rekursif(x,y):
    if(y == 0):
        return 1
    else:
        return x * rekursif(x,y-1)


print(rekursif(100,2))