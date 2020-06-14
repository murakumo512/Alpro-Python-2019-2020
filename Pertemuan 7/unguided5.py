def hitung_satuan(angka):
    strx = str(angka)
    for i in range(4):
        if i == 0:
            print(strx[i], "ribuan")
        if i == 1:
            print(strx[i], "ratusan")
        if i == 2:
            print(strx[i], "puluhan")
        if i == 3:
            print(strx[i], "satuan")


hitung_satuan(4590)