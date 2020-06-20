def tambah(nama, sks, ruang):
    dd = dict()
    if sks == "":
        sks = 0
    if int(sks) <= 0:
        sks = 0
    if ruang.strip() == "":
        ruang = "-"
    if  nama.strip() == "":
        nama = "-"
    sks1 = str(sks)
    dd["nama"] = nama.strip()
    dd["sks"] = sks1.strip()
    dd["ruang"] = ruang.strip()

    return dd



nama = 'Alpro'
sks = 3
ruang = '   '
hasil = tambah(nama, sks, ruang)
print(hasil['nama'])
print(hasil['sks'])
print(hasil['ruang'])
