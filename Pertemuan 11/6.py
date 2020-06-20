barang = {
    "b001" :{
        "nama":"buku",
        "harga" : 5000,
    },
    "b002":{
        "nama" : "pensil"
        "harga" : 1000,
    }
}


for key in barang:
    for nest_key in barang[key]:
        print(nest_key, ':', barang[key][nest_key])