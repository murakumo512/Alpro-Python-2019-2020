numberlist = {}
numberlist[3] = 3
numberlist['3'] = 3
numberlist[3.0] = 3

min = 333
for i in numberlist:
    min -= numberlist[i]
print(min)