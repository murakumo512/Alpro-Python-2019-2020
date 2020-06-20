def faktor(n):
    if n == 0:
        return 1
    else:
        return n * faktor(n-1)
    
print(faktor(3)+2)