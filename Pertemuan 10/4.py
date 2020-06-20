mahasiswa = {
    "nama": "bambang",
    "nim" : "71180001",
    #"umur" : 18,
    "prodi" : "Informatika",
    "asal" : "Sembir"
}


for key in mahasiswa:
    print(key, end=' ')
if "asal" in mahasiswa:
    del mahasiswa["asal"]
else:
    pass

for x in mahasiswa.values():
    print(x)