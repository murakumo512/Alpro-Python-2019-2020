def komb(a,b):
    hasil=faktorial(a)/(faktorial(a-b)*faktorial(b))
    return hasil


def faktorial(n):    
    if n==0 or n==1:
        hasil=1
        return hasil
    else:
        hasil=faktorial(n-1) * n
        return hasil

print(komb(10,3))