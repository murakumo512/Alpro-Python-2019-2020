def hittotal(brg):
    barang = brg.copy()
    barang["stok"] = 200
    barang["harga"] = 1500
    total = brg["stok"]*brg["harga"]
    print(total)

barang = {
    "nama" : "pensil",
    "kode" : "B001",
    "harga" : 1000,
    "stok" : 100
}
hittotal(barang)