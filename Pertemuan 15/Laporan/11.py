import re

def cari(a,b):
    match = re.search(a, b)
    if match:
        print("ketemu")
    else:
        print("ga ada")  



a = input("kata yang dicari :")
b = input("kalimatmu : ")
cari(a,b)