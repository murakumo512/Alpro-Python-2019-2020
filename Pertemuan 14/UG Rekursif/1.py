def desimaltobinary(n):  
    convertString = "01" 
    if n < 2:  
        hasil=convertString[n]   
        return hasil
    else:    
        hasil=  desimaltobinary(n//2) + convertString[n%2]
        a=hasil[0:len(hasil)-1]
        hasil= hasil[len(hasil)-1]+a
        return hasil
print(desimaltobinary(2))