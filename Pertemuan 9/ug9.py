def email_function(subject_email):
    print("Daftar subject email:")
    panjanglist = len(subject_email)
    dd = " "
    bb = dd.join(subject_email)

    for i in range(0,panjanglist):
        for j in range(0,len(subject_email[i])):
            #aa = subject_email[j]
            #print(aa)
            print("Daftar subject email setelah filter:")







subject_email = [
["Kencan", "Sabtu"],
["Tugas", "menulis", "Esai"],
["Belanja", "online", "diskon", "sekarang"],
["Beli", "buku", 2, "saja"]
]
email_function(subject_email)