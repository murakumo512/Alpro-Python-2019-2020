def rekursif(angka, angka2):
    if(angka2 == 0):
        return 1
    else:
        return angka*rekursif(angka, angka2-1)
    
print(rekursif(22,5))