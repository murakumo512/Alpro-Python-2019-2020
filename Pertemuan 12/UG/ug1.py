def cek_kalimat(kalimat):
    konsonan=['B','C','D','F','G','H','J','K','L','M','N','P',
              'Q','R','S','T','V','W','X','Y','Z']

    kata = "saya 1"
    dic=dict()
    kalimat=kata.split()
    vokal =["a","i","u","o","e"]
    angka = ["0","1","2","3","4","5","6","7","8","9"]
    print(len(kalimat))
    for jj in range(0,len(kalimat)):
        for i in range(0,len(kalimat[jj])):
            if kata[i] in vokal:
                if kata[i] not in dic: #cek apakk ada di dict
                    dic[kata[i]] = 1 # pertama
                else:
                    dic[kata[i]] += 1 # +1

            if kata[i] in angka:
                if kata[i] not in dic: #cek apakk ada di dict
                    dic[kata[i]] = 1 # pertama
                else:
                    dic[kata[i]] += 1 # +1
    for key, val in list(dic.items()):
        print(key,val)

kalimat = 'Dalam 1 hari budi makan 3 kali.'
hasil = cek_kalimat(kalimat)