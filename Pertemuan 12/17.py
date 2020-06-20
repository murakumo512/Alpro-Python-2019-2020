tup = [('a', (10,20,30)),('b',(40,50,60)),('c',(70,80,90))]
for k in tup:
    if 'a':
        print(k[:-1]+(100,))
    elif 'b':
        print(k[::-1]+('xx',))
    else:
        print(k[:-3]+55(55,))