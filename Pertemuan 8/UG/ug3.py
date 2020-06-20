def trapesium () : #ini adalah sebuah fungsi untuk mengerjakan luas trapesium
    #t = int(input("Masukkan tinggi : "))
    #j = int(input("Masukkan jumlah sisi sejajar : "))
    #l = int(t * j / 2) #ini rumus
    #print ("Jadi luas trapesium adalah : ", l, ("\n")) #ini resultny
    array = []
    total = 0
    benar = 0
    while benar == 0:
        i = int(input("Masukkan data : "))
        if i <= 12:
            benar = 1
    for x in range (i):
        nilai = int(input("Masukkan nilai ke {}: ".format(x+1)))
        array.append(nilai)
    pph = 0
    totalpph = []
    print("------------------------------------------------")
    print("Bulan"," ","Penghasilan"," ","PPH")
    for j in range (0,i):
        pph+=5
        totalpph.append(pph)
        print(j+1,"        ", "$%d"%array[j], "      ", "$%d"%pph)
        
    print("------------------------------------------------")

    

    print("Total Penghasilan : ",format(sum(array)))
    print("Total PPh : ", format(sum(totalpph)))


trapesium()