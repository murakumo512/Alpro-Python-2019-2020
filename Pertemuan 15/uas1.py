import numbers
import re
import random

def angka_berbeda(data):
    for i in data:
        print(i)
        for j in i:
            if j == 6:
                print(j)
    mylist = list(dict.fromkeys(data))
    mylist.sort()
    panjang=len(mylist)
    print(mylist)
    return panjang



data = [4, 8, 9, 4, 6, 6, 8, 3, 2, 9, 2, 6, 2]
hasil = angka_berbeda(data)
print(data)
print(hasil)