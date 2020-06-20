def a(angka1,angka2):
    return angka1 if angka1 > angka2 else angka1+(a(angka1+1, angka2))

print(a(5,4))