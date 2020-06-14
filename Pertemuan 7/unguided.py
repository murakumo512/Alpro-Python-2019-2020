def penghitung_kata(caption):
    jadikan_list = caption.split()
    hitung_kata = len(jadikan_list)
    listtag = []
    jumlahtag = 0
    print("Caption yang dimasukkan : ", caption)
    print()
    print("Pengguna yang di-tag")
    for i in range(hitung_kata):
        kata = jadikan_list[i] 
        if kata[0] == '@':
            jumlahtag+=1
            listtag.append(kata)
    print("--------------------")
    for i in range(jumlahtag):
        print(listtag[i])
    print("--------------------")
    print("Jumlah username yang di-tag :", jumlahtag)



caption = input('Masukan Kata: ')
penghitung_kata(caption)