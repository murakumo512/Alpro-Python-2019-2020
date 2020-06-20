def daftar_tidak_sama(angka1, angka2, batas):
    lst1 = list()
    lst2 = list()
    for i in range(1,batas):
        if i % angka1 == 0:
            lst1.append(i)
        if i % angka2 == 0:
            lst2.append(i)
    s1 = set(lst1)
    s2 = set(lst2)
    s2 = s1 ^ s2
    print(len(s2))

daftar_tidak_sama(7, 3, 30)
