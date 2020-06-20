nama = ""
def rekursif(angka1, angka2):
    if(angka1==angka2):
        return 1
    else:
        if(nama[angka1]!=nama[angka2]):
            return 0
        else:
            return rekursif(angka1+1, angka2-1)
nama = "katak"
print(bool(rekursif(0,len(nama)-1)))