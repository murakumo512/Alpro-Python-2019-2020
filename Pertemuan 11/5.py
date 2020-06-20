def tambah(mhs):
    mhs["umur"] = 20
    print(mhs.get("umur"))

mahasiswa ={
    "nama": "bambang",
    "nim" : "71180001",
    "umur" : 18,
    "prodi" : "Informatika",
    "asal" : "Sembir"
}

x = mahasiswa.keys()
print(x(1))

#if "asal" in mahasiswa:
#    print("ada")
#else:
#    print("b")
#print(mahasiswa["nama"])
#print(mahasiswa.pop("nama"))
#print(mahasiswa.get("nama"))