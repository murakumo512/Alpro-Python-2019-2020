def soal1():
    deret = [] #ini buat listnya nilainya
    #i = int(input("Masukkan jumlah data : ")) #masukann banyaknya data

    i = 1
    x = 0 #berikan nilai awa 0
    y = 0
    while x < i: #selama x kurang dari i
        nilai = input("Masukkan nilai ke {}: ".format(y+1))
        y+=1
        if (nilai == "stop" or nilai == "Stop"): 
            x+=1#outpunya akan masukan nilai ke 1, karena x+1
        else:
            deret.append(int(nilai))

    print("nilai max",format(max(deret)))
    print("nilai min",format(min(deret)))

#soal1()


def soal2():
    A = 4
    B = 3
    C = 2
    D = 1
    SKS = 3
    ini_array = []
    totalgrade1 = 0
    totalgrade = 0

    n = int(input("Jumlah mata kuliah : "))
    for x in range(n):
        nilai = input("Nilai MK {} : ".format(x+1))
        if nilai == "A" or nilai == "a":
            totalgrade = 4
        if nilai == "B" or nilai == "b":
            totalgrade = 3
        if nilai == "C" or nilai == "c":
            totalgrade = 2
        if nilai == "D" or nilai == "d":
            totalgrade = 1
        totalgrade1 = totalgrade1 + totalgrade

    print("total : %.2f " % (totalgrade1/n))


#soal2()


def soal3(i,q):
    deret = [] #ini buat listnya nilainya
    #i = int(input("Masukkan jumlah data : ")) #masukann banyaknya data

    #i = int(input("Masukkan nilai 1 : "))
    #q = int(input("Masukkan nilai 2 : "))
    x = 0 #berikan nilai awa 0
    y = 0
    while x < i: #selama x kurang dari i
        x +=1 #increasing x
        y = y + q #lakukan penjumlahan y, perulangan hingga x = i. Jika x = i maka keluar dari perulangan
    print(y)

#print("Perkalian tanpa operator *")
#soal3(2,4)

def soal4(q,i):
    #q sebagai bilangannya
    #i sebagai pemangkatnya
    x = 0
    y = 1 #y adalah hasil perkalian, nilai awalnya 1
    while x < i: #lakukan perulangan sebanyak i
        x +=1 #increasing x
        y = y * q #lakukan perkalian bilangan, perulangan hingga x = i. Jika x = i maka keluar dari perulangan
    print(y) #print hasil pemangkatan

#print("pangkat tanpa operator **")
#soal4(2,8)

# Program python untuk menentukan bilangan prima atau tidak
# Meminta input bilangan dari user
def prima(num):
    #num = int(input("Masukkan bilangan: "))
    # bilangan prima harus lebih besar dari 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "bukan bilangan prima")
                break
        else:
            print(num,"adalah bilangan prima")
    # bila bilangan kurang atau sama dengan satu
    else:
        print(num, "bukan bilangan prima")

#print("test case Prima bukan")
#prima(12)





def average():
    array = [] #array kosong
    total = 0

    n = int(input("Masukkan banyaknya elemen array: ")) #mendeklarasikan variable n dan menginputkan banyaknya data kedalam variable n oleh user.

    for x in range(n):
        nilai = float(input("Masukkan nilai ke-{} : ".format(x+1)))#melakukan perulangan sebanyak n dan menginputkan nilai dari setiap data lalu dimasukkan kedalam variable array.
        array.append(nilai)#melakukan perulangan sebanyak n dan menginputkan nilai dari setiap data lalu dimasukkan kedalam variable array.

    print("\nHasil nilai total adalah : {}".format(sum(array))) #menampilkan hasil total nilai dengan menggunakan fungsi sum dari variable array dan nilai rata-rata dari hasil operasi total dibagi jumlah variable n.
    print("Hasil rata-rata adalah : {}".format(sum(array)/n)) #menampilkan hasil total nilai dengan menggunakan fungsi sum dari variable array dan nilai rata-rata dari hasil operasi total dibagi jumlah variable n.

#average()


def huruf_urut():
    text = "Riel Ganteng"
    for huruf in text:
        print(huruf)
#huruf_urut()

def nama_list():
    list_nama = ['Riel', 'Mardonius']
    for nama in list_nama:
        print("Nama : ", nama)

nama_list()