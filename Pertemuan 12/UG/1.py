def count_consonants(kalimat):
    kalimat = kalimat.lower();
    consonants = list("bcdfghjklmnpqrstvwxyz")
    vocal = list("aiueo")
    angka = list("0123456789")
    inikonsonan = sum(kalimat.count(aaa) for aaa in consonants)
    inivocal = sum(kalimat.count(aaa) for aaa in vocal)
    iniangka = sum(kalimat.count(aaa) for aaa in angka)
    hasil = dict()
    hasil["konsonan"] = inikonsonan
    hasil["vokal"] = inivocal
    hasil["angka"] = iniangka
    return hasil

test_str="Dalam 1 hari budi makan 3 kali"
hasil=count_consonants(test_str)
print(hasil['vokal'])
print(hasil['konsonan'])
print(hasil['angka'])
