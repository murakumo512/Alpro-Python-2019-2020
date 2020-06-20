angka = 0 
def cek(pembagi):
    if(pembagi == 1):
        return("prima")
    elif(angka % pembagi == 0 ):
        return("bukan prima")
    else:
        return cek(pembagi-1)
angka = 6
print(cek(angka-1))