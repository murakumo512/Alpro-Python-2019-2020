my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


panjanglist = len(daftar_ikan)
    #print(panjanglist)
    print("Daftar ikan dengan jumlah", panjanglist,":")
    for a in range(0,panjanglist):
        print(daftar_ikan[a])
    print()
    print("Daftar ikan setelah dicek:")
    for i in range(0,panjanglist):
        aaa = daftar_ikan.count(daftar_ikan[i])
        #print(aaa)
        if aaa > 1:
            print(daftar_ikan[i])
        else:
            print(daftar_ikan[i] + " unique")