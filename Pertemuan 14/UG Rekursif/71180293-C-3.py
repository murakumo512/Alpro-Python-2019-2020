def bagidesimal(a):
    x = a.split(".")
    a = ""
    #baru = ""
    for i in range (0,len(x)):
        conv = toStr(int(x[i]))
        for j in range(0,8-len(conv)):
            conv = "0" + conv
        if i<len(x)-1:
           a = a + conv + "."
        else:
            a = a + conv 
    hasil = a
    return hasil

def toStr(n):  
    convertString = "01" 
    if n < 2:  
        hasil=convertString[n]   
        return hasil
    else:    
        hasil=  toStr(n//2) + convertString[n%2]
        return hasil

print(bagidesimal("192.168.1.2"))
