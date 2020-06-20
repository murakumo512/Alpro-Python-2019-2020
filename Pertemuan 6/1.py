a = 10
b = 13
c = 0
while a < b :
    a = a + 1
    if a % 2 == 0:
        c = c + a**2
        c = c - b**2

print(c)