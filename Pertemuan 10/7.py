numberlist = {}
numberlist[5] = 5
numberlist['5'] = 1
numberlist[5.0] = 3

sum = 0
for i in numberlist:
    sum += numberlist[i]
print(sum)