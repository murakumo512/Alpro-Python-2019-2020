def myfucn(a,b):
    if a > 3:
        return b,a
    else:
        return a,b

swap = myfucn

for i in range(6):
    i,s = swap(i,0)
    print(i)