def surprise(a,b):
    num = a**2 + b
    return num

c = 3
d = 0
while c > 0:
    d = surprise(c,7)
    print(d)
    c = c -1
print(d)