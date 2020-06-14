a = int(input("angka"))
b = 0
c = 0
while a > 0:
    if a % 2 or a % 3 == 0:
        b = a + b
    else :
        c = a * a
    a = a - 1
print(b,c)