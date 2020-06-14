

 # Menghitung jumlah huruf konsonan
def hitung_jumlah(string):
    kecilower=['b','c','d','f','g','h','j','k','l','m','n',
              'p','q','r','s','t','v','w','x','y','z',
              'a','i','u','e','o']
    besaruper=['B','C','D','F','G','H','J','K','L','M','N','P',
              'Q','R','S','T','V','W','X','Y','Z','A','I','U','E','O']
    spaser = [' ']
    hitung = 0
    hitung1 = 0
    hitung2 = 0
    for i in string:
        if i in besaruper:
            hitung+=1
        if i in kecilower:
            hitung1+=1
        if i in spaser:
            hitung2+=1
    print("Jumlah huruf kecil :", hitung1)
    print("Jumlah huruf besar :", hitung)
    print("Jumlah spasi :",hitung2)

hitung_jumlah("Saya Lapar  dunk")