 # Menghitung jumlah huruf vokal


 # Menghitung jumlah huruf konsonan
def cari_UKDW(kalimat):
    hkonsonan=['U','u','K','k','D','d','W','w']
    hitung=0
    d = 0
    k = 0
    w = 0
    u = 0
    for i in kalimat:
        if i in hkonsonan:
            hitung+=1
            if i == "d" or i == "D":
                d+=1
            if i == "k" or i == "K":
                k+=1
            if i == "w" or i == "W":
                w+=1
            if i == "u" or i == "U":
                u+=1

    print("Jumlah huruf U/u :", u)
    print("Jumlah huruf K/k :", k)
    print("Jumlah huruf D/d :", d)
    print("Jumlah huruf W/w :", w)

cari_UKDW("Saya kuliah di 1 UKDW!")