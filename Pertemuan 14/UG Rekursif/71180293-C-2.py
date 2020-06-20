def faktorialganjil(jumlah,awal):
    jumlah = jumlah*2  
    ha = f(jumlah,awal)
    return ha

def f(jumlah,awal): 
    if jumlah == 1 or jumlah==1:
        #print(jumlah)
        return 1
    else:
        if jumlah % 2 != 0:
            hasil=f((jumlah)-1,awal)*jumlah
            #print(jumlah)
            return hasil
        else:
            return f((jumlah)-1,awal)


print(faktorialganjil(10,0))