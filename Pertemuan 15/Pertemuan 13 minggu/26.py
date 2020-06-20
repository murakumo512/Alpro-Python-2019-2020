def rekursif(x,y):
    return x if y == 0 else rekursif(y, x % y)

print(rekursif(10,20))


a = set()
a.add("432")
a.add(True)

print(a)