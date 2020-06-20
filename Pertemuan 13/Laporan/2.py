Data= ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')
print(Data[0])
print(Data[1])
print(Data[2])
str1, str2, str3 = Data
print(str1)

tpl=tuple(str2)
aa=tuple(str1)
print (tpl)
ls=list()
ls=str1.split()
print(ls)
ter=ls[::-1]
ter1=tuple(ter)
print("nama depan : " ,aa[1:8])
print ("Nama terbalik : ",ter1)

#name = ("Jaka", "Joko", "Jono")
# using slicing technique
#rev_name = name[::-1]
#rev2= name[::-3]
#print("urutan: ", name)
#print("urutan_terbalik: ", rev_name)
#print("urutan_terbalik: ", rev2)