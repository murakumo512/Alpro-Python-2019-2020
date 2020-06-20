num = [10,20,(10,20),30]
count = 0
for i in num :
    if isinstance(i, tuple):
        break
    count += 1

print(count)