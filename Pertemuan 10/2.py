def ubah(a):
    maha = a.copy()
    maha["prodi"] = "sistem in"
    a = dict(maha)
    print(a.get("prodi"))
def tambah(a):
    maha = dict(a)
    a["umur"] = 20
    print(a.get("umur"))

def getnim(mhs):
    return mhs("mhs")

maha = {
    "nama": "bambang",
    "nim" : "71180001",
    #"umur" : 18,
    "prodi" : "Informatika",
    "asal" : "Sembir"
}

#ubah(maha)
#print(maha.get("prodi"))
#print(maha.pop("prodi"))
#print()
tambah(maha)
print(maha.get("umur"))
#print()
#maha.pop("umur")
#print(maha.get("asal"))


if "asal" in maha:
    del maha["asal"]
else:
    pass

for x in maha.values():
    print(x)