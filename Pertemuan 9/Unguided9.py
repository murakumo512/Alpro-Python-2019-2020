def fish_function(daftar_ikan):
    panjanglist = len(daftar_ikan)
    #print(panjanglist)
    print("Daftar ikan dengan jumlah", panjanglist,":")
    for a in range(0,panjanglist):
        print(daftar_ikan[a])
    print()
    print("Daftar ikan setelah dicek:")
    for i in range(0,panjanglist):
        aaa = daftar_ikan.count(daftar_ikan[i])
        #print(aaa)
        if aaa > 1:
            print(daftar_ikan[i])
        else:
            print(daftar_ikan[i] + " unique")


def email_function(subject_email):
    print(subject_email[0:2])






subject_email = [
["Kencan", "Sabtu"],
["Tugas", "menulis", "Esai"],
["Belanja", "online", "diskon", "sekarang"],
["Beli", "buku", 2, "saja"]
]
email_function(subject_email)








daftar_ikan = [
"nila",
"Nila", 
"Lele", 
"Salmon", 
"Lele", 
"Lele", 
"Koi", 
"Bawal"
]

fish_function(daftar_ikan)