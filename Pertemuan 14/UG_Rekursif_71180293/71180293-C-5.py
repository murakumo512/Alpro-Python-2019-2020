def dig(digit):
      #buat jaga2 kalau untuk konver ke base yg lain
	angka = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] 
	for x in range(15):
		if digit == angka[x]:
			return x

def jum(a):
    aa = str(a)
    if len(aa) == 1:
    #rint(aa)
        hasil = int(dig(aa))
        return hasil
    else:
        pj = len(aa)
        xx = int(dig(a[0]))
        bb=int(xx) * (2 ** (pj-1))  #2 =base
    #print("vv",bb)
        hasil = bb + int(jum(aa[1:pj]))   #rekursif
        return hasil
        
def bagidesimal(biner):
    lstBiner = biner.split(".") #dalam bentuk list
    dec = ""
    for i in range(len(lstBiner)):
        if i == len(lstBiner) - 1:
            dec = dec + str(jum(lstBiner[i]))
        else:
            dec = dec + str(jum(lstBiner[i])) + "."
    return dec

print(bagidesimal("11000000.11000001.11011000.00000001"))