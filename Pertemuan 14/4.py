def rekur(angka, angka2):
    if(angka2==0):
        return 1
    else:
        return angka*rekur(angka,angka2-1)

print(rekur(100,2))