def konversi(kalimat):
    lst = kalimat.split()
    judul, penerbit = kalimat.split('diterbitkan')
    #print(judul)
    #print(penerbit)
    d = dict()
    d['judul'] = judul.strip()
    d['penerbit'] = penerbit.strip()
    return d

kalimat = 'Logika Matematika diterbitkan Andi Publisher' 
hasil = konversi(kalimat)
print(hasil['judul'])
print(hasil['penerbit'])


#email = 'didanendya@ti.ukdw.ac.id'
#username, domain = email.split('@')
#print("username : ",username)
#print("Domain : ",domain)
