s = input("input : ")
kata = input("input kata yang dicari ada: ")
uppers = s.upper()
upperkata = kata.upper()
l = uppers.split()
jumlahkata = len(l)
araybaru = []
print(l)
for i in range(jumlahkata):
    aa = l[i]
    ll = ""
    for j in range(len(l[i])):
        if aa[j] != ".":
            ll = ll + aa[j]
    araybaru.append(ll)

print("array baru",araybaru)
for a in range(len(araybaru)):
    print(araybaru[a], end=' ')
cacah = 0
for i in range(jumlahkata):
    if araybaru[i] == upperkata:
        cacah+=1
print(kata,"ada", cacah, "buah")













