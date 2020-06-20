#############
#latihan 1
dick=dict()
lstanggota=list()
group=int(input("Jumlah group:"))
anggota=int(input("jumlah anggota / group:"))

for x in range(0,group):
  namagrp=input("nama group ")
  for j in range(0,anggota):
    nmanggota=(input("nama anggota:"))
    lstanggota.append(nmanggota)
  dick[namagrp]=lstanggota
  lstanggota=list()
#masukan anggota dalam list
print(dick)
angg=[]
for ang in dick.values():
  angg.append(set(ang))
print("angg :",angg)
print(angg[0])

#intersect
hasil=angg[0]

for kk in (1,len(angg)-1):
  #hasil=hasil & angg[kk]
  qqq=hasil.intersection(angg[kk])
print("intersection :",qqq)

#symdiff
hasil=angg[0]

for kk in (1,len(angg)-1):
  qqq=hasil.symmetric_difference(angg[kk])
print("sym diff :",qqq)
##coy tolong dicoba yah
