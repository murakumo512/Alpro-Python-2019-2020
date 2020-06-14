i = 7
while i < 100:
    print(i)
    i = (i**2) + 3
    if i % 2 == 0:
        i = i +i
print(i)