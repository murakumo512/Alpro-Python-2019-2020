def cari_apd(daftar_apd,nama):
    daftar_apd.sort(reverse=True)
    print("DAFTAR KETERSEDIAAN APD :")
    print(daftar_apd)
    for i in range (0,len(daftar_apd)):
        if (daftar_apd[i][0])==nama:
            print("Hasil Perncarian :")
            print(nama, "sejumlah", daftar_apd[i][1], "buah")


daftar_apd=[('Masker Bedah', '1500'),('Face Shield', '1500'),('Masker N95', '10001'),('Baju Hazmat', '1500'),('Sarung Tangan', '125')]
cari_apd(daftar_apd, 'Sarung Tangan')