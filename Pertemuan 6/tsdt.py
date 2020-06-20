def gambar_persegi_panjang(tinggi,lebar):
    for i in range(0,tinggi):
        if i > 0 and i < tinggi-1:
            for j in range (0,lebar):
                if j > 0 and j < lebar-1:
                    print("")
                else:
                    print(j)
        else:
            for j in range(0,lebar):
                print (j)
        print()


tinggi = int(input("tinggi : "))
lebar = int(input("lebar : "))
gambar_persegi_panjang(tinggi, lebar)
print("1 2 3 4")
print("5 6 7 8")
print("9 10 11 12")
print("13 14 15 16")
print("17 18 19 20")


for i in range(7):
    for j in range(5):
        if (i==0 or i==4) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end="")
    print()