def rekur(x,y):
    return x if y == 0 else rekur(y,x % y)

print(rekur(10,20))