#Conversi List ke Set

#List menjadi set
L=[1,"2",3]
S=set(L)
print("Data dalam list :",L)
print("List tunggal ke Set",S)
zz=list()

#Jika lsit dalam list -->set
L=[1,"2",["a","b"]]
print("Data dalam list in list :",L)
for i in L:
  if len(str(i))>2: #if anggota L is list
    L1=set(i)  #list menjadi tuple
    zz.append(tuple(L1)) #tambahkan dalam list baru
  else: #if anggota L is tunggal
    zz.append(i) #tambahkan dalam list baru
print("Hasil Set : ",set(zz)) # rubah list yg baru ke set

print()

#Conversi Set to List

#Set menjadi list
SetX= {1, 3, '2'}
sToL=list(SetX)
print("Set :",SetX)
print("Set to List : ",sToL)
print()
sToL=list()
SetX= {1, ('b', 'a'), '2'}
for qq in SetX:
  #print(qq)
  if len(str(qq))>2:
    sToL.append(list(qq))
  else:
    sToL.append(qq)
print("Set :",SetX)
print("Set to List : ",sToL)

print()

#conversi tuple to set
#set tidak mau kalau bentuk begini {1,3,"2",["a","b"])
#set mau kalau bentuk begini {1,3,"2",("a","b"))


#Tuple to Set
TupX= (1, 3, '2')
tToS=set(TupX)
print("Tuple : ",TupX)
print("Tuple to Set : ",tToS)

TupX= (1, 3, '2',("a","b"))
tToS=set(TupX)
print("Tuple : ",TupX)
print("Tuple to Set (ada tuplenya)  : ",tToS)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

tTos=set()
pan=len(TupX)
lst=list()
for qq in TupX:
  if len(str(qq))>2:
     lst.append(list(qq))
  else:
    lst.append(qq)
print("dlm List:",lst)
print("kalau list dalam list mau dijadikan Set, akan error")
print("maunya : {1,3,'2',['a','b']}")
for a in range(0,len(lst)-1):#list ["a,"b] tidak ikut (kalau begini mau), tapi kalau ada list di dalam set, tidak mau
  tTos.add(lst[a])
print("Tuple to Set (tidak ada listnya)  : ",tTos)

#for a in range(0,len(lst)):#list ["a,"b] ikut kalau begini  tidak mau
#  tTos.add(lst[a])
#Sprint("Tuple to Set (ada listnya) <error> : ",tTos)


print()

#set ke tuple
thisset = {1,2,3}
sTot=tuple(thisset)
print(sTot)

thisset = {1,2,3,("a","b")}
sTot=tuple(thisset)
print("Bentuk asli set :",thisset)
print("Bentuk Tuple tuple:",sTot)

ss=list()
thisset = (1,2,3,["a","b"])
for i in thisset:
	ss.append(i) 
sTot=tuple(ss)
print("Bentuk Tuple list:",sTot)

print()
