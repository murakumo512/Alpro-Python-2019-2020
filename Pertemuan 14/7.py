def rekur(angka, angka2):
    return angka if angka > angka2 else angka+(rekur(angka+1, angka2))
print(rekur(5,4))