import re
kamus = (
    ('p', 'h'),('h', 'p'),
    ('k', 'ny'),('ny', 'k'),
    ('r', 'y'),('y', 'r'),
    ('c', 'j'),('j', 'c'),
    ('n', 'dh'),('dh', 'n'),
    ('p', 'h'),('h', 'p'),
    ('d', 'm'),('m', 'd'), 
    ('t', 'g'),('g', 't'),
    ('s', 'b'),('b', 's'),
    ('w', 'th'),('th', 'w'),
    ('l', 'ng'),('ng', 'l'),)

  #("p","h") ==> p=asal  h=arti

def carikamus(isi_kamus, ygdicari):
    try: #cari apakah bilai x pada tuple  = nilai yg dikirim, return = nilai y
        return next(arti for asal, arti in isi_kamus if asal == ygdicari)
    except StopIteration: #kalau tddak ketemu 
        return "a"

def ubah(text):
    text=text.lower()
    lst=re.findall(".",text)  #masuj ke list
    walik=""
    for a in range(0,len(lst)):  # proses perulangan ganti huruf per huruf
        qq=(carikamus(kamus, lst[a]))  #cari di kamus
        #print(qq)
        if qq== "a":  #jika volal 
            walik=walik+lst[a] # susun yg baru tidak ada yg di rubah
        else:
            walik=walik+qq # jika ada di kamus, susun yg baru dengan perubahan
    walik=walik+" " #jika ganti kata, tambahkan spasi
    print(walik)
text="berkobar karena cinta kepada rumahmu"
ubah(text)