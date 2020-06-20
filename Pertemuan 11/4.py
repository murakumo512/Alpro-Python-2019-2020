jumlah = dict()
ukuranbaju = ["L", "M", "XL",  "L", "M" ]
for ukuran in ukuranbaju:
    if ukuran not in jumlah:
        jumlah[ukuran] = 1
    else:
        jumlah[ukuran] +=1


print(jumlah)


angka = 102
print('Angka = %s'% angka)