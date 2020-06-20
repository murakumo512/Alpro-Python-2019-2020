def hitTotal(brg):
    barang = brg.copy()
    barang["stok"] = 200
    barang["harga"] = 1500
    total = barang["stok"]*barang["harga"]
    print(total)

barang = {
    "nama" : "pensil",
    "kode" : "b001",
    "harga" : 1000,
    "stok" : 100
}

hitTotal(barang)

a = open("a.txt", "r")