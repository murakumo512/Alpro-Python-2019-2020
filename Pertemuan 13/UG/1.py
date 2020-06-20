def tampilkan(kalimat1,kalimat2):
    kalimat1 = kalimat1.strip()
    kalimat2 = kalimat2.strip()

    set1=set(kalimat1.lower())
    set2=set(kalimat2.lower())
    gab=set1 | set2
    lst = list(gab)
    lst.sort()
    for i in range(len(lst)-1):
        print(lst[i],end=',')
    print(lst[i+1])
tampilkan("  Beyek","bebek  ")


