import re

def sortirProses(txt):
    list1 = re.findall("([1])", txt)
    print("Lokasi1: ",len(list1),"barang")
    list2 = re.findall("([2])", txt)
    print("Lokasi2: ",len(list2),"barang")
    list3 = re.findall("([3])", txt)
    print("Lokasi3: ",len(list3),"barang")  

txt = """RRRU3 YU3RR FJK2 JD2K
HHS1EE HJRR2 HH2JJM UU1UI 3JJI
YY1EER"""
sortirProses(txt)