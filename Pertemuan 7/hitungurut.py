def urutangka(a,b,c):
    aa = int(a)
    bb = int(b)
    cc = int(c)
    for i in range(aa,bb+1,cc):
        if i % 2 == 0:
            for j in range (0,i):
                print(i, end='')
            print()


#a = input("masukkan angka awal : ")
#b = input("masukkan angka akhir : ")
#c = input("masukkan berapa lompatan : ")
#urutangka(a,b,c)

def urutangkakotak(x):
    #xx = int(x)
    #yy = int(y)
    for j in range(1,x+1):   
        if j %2 == 0:
            for i in range(x,0,-1):
                print(i,end='')
        else:
            for i in range(1,x+1):
                print(i,end='') 
        print()        

#urutangkakotak(5)

#my_num=str(input("Enter the number to be reversed: "))
#print("Reverse of the given number is: ")
#print(my_num[::-1])

def urutangkasegitisikubawh(z):
    for j in range(1,z+1):
        aa = z+1-j
        for i in range(aa):
            if i %2 == 0:
                print("X",end='')
            else:
                print("O", end='')
        print()

#urutangkasegitisikubawh(6)


def urutsegi(y):
    for j in range(1,y+1):
        for i in range(1,y+1):
            if (y + 1 - j) > i:
                print(" ", end='')
            else:
                print("x", end='')
        print()




def uratsegi(y):
    j = 1
    i = 1
    while j < y+1:
        while i < y+1:
            if(y + 1 - j) > i:
                print(" ", end='')
            else:
                print("x", end='')
            i+=1
        print()
        i = 1
        j+=1
#uratsegi(6)


def baris(x,y):
    x = 0
    for i in range(x,y):
        w = input("Brs ke {}: ".format(i+1))
        print("baris ke {} adalah".format(i+1))
    

baris(0,2)

compare_digest(a, b)