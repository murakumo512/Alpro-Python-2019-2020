def panjang(n):
    array1 = ["A","B","C","D","E",
            "F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S",
            "T","U","V","W","X","Y","Z"]
    fh = open('alfabet.txt', 'w')

    x = 0
    asd = ""
    for i in range(0,26):
        print(array1[i], end='')
        asd = asd + array1[i]
        x+=1
        if x == n:
                print()
                fh.write(asd)
                fh.write("\n")
                asd = ""
                x = 0
    fh.write(asd)
    fh.close
                
n = int(input("Masukkan panjang huruf: "))
panjang(n)

