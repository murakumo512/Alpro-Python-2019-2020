def soal1():
    kalimat1=[]
    kalimat2=[]
    Jmlbaris1=0
    Jmlbaris2=0

    bacafile = '1.txt'  
    with open (bacafile,'r') as fp:  
        line = fp.readline()
        kalimat1.append(line.strip())
        Jmlbaris1=Jmlbaris1+1
        while line:
           #print(line.strip())
            line = fp.readline()
            kalimat1.append(line.strip())
            Jmlbaris1=Jmlbaris1+1
    #print (kalimat)
    bacafile = '2.txt'  
    with open (bacafile,'r') as fp:  
        line = fp.readline()
        kalimat2.append(line.strip())
        Jmlbaris2=Jmlbaris2+1
        while line:
       #print(line.strip())
            line = fp.readline()
            kalimat2.append(line.strip())
            Jmlbaris2=Jmlbaris2+1

    if Jmlbaris1>Jmlbaris2:
        Jmlbaris=Jmlbaris1
    else:
        Jmlbaris=Jmlbaris2
    hasil=[]
    for i in range (0,Jmlbaris-1):#sebanyak jml baris  
        if kalimat1[i] == kalimat2[i]:
            hasil.append("sama")
    #print ("sama")
        else:
            hasil.append("beda")
    #print("beda")
    print("Isi file 1:")
    for i in range (0,Jmlbaris-1):#sebanyak 
        print (kalimat1[i])
    print()
    print("Isi file 2:")
    for i in range (0,Jmlbaris-1):#sebanyak 
        print (kalimat2[i])
    print()
    print("perbandingan Isi file 1 dan 2:")
    for i in range (0,Jmlbaris-1):#sebanyak 
        print ("Baris ", i+1, " ", hasil[i])
#soal1()




def soal2():
    kalimat=[]
    Jmlbaris=0
    bacafile = 'soal.txt'  
    with open (bacafile,'r') as fp:  
        line = fp.readline()
        kalimat.append(line.strip())
        Jmlbaris=Jmlbaris+1
        while line:
       #print(line.strip())
            line = fp.readline()
            kalimat.append(line.strip())
            Jmlbaris=Jmlbaris+1
#print (kalimat)
    for i in range (0,Jmlbaris-1):#sebanyak jml baris
        txt=kalimat[i]
        panjang = len(txt)
        x = txt.rfind("||") #cari letak tanda ||
        sisa = panjang -(x+3)
        soal = txt[0:x].strip()
        jawaban=txt[x+3:panjang].strip()
        print("Soal: ",soal)
        x = input('Jawaban Anda :')
        if x == jawaban:
            print("Jawaban: Benar")
        else:
            print("Jawaban: salah")
        print()
    fp.close

#soal2()





print("Selamat datang di Program Biodata")
print("=================================")

# Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks
teks =("Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat))

# buka file untuk ditulis
file_bio = open("biodata.txt", "w")

# tulis teks ke file
file_bio.write(teks)


# tutup file
file_bio.close()



