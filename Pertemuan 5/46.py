nim1  = int(input("nim1 : "))
nim2  = int(input("nim2 : "))
if(nim1<nim2):
    nimDipakai = nim1
else:
    nimDipakai = nim2
if(nimDipakai%2==0 and nimDipakai!=0):
    print("kerjakan soal A")
elif(nimDipakai%2!=0) and nimDipakai!=0:
    print("kerjakan soal b")
else:
    print("gajkelas")
print("selamat")