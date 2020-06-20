c = 0
for x in range(0,13):
    if (x+1) % 2 == 0:
        print('*')
        c+=1
    else:
        print('*'*13)
        c+=13
print(c)