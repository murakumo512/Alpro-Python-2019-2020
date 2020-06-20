def a(angka):
    if(angka == 0  or angka == 1):
        return angka
    else:
        return (a(angka-1) + a(angka-2))

print(a(50))