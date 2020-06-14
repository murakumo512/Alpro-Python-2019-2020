def penghitung_kata(caption):
    jumlahhuruf = len(caption)
    print(jumlahhuruf)
    kata = ""
    array1 = []
    for i in range(0,jumlahhuruf):
        huruf = caption[i]
        if caption[i] != " ":
            kata = kata + huruf
        else:
            print(kata)
            print(len(kata))
            array1[1] = kata
            kata = ""
            
    print(kata)
    print(len(kata))   
    array1[2] = kata

    print(array1[1])
    print(array1[2])
    print("Caption yang dimasukkan : ", caption)
caption = input("")
penghitung_kata(caption)