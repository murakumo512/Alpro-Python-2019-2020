def ganti_vokal(string):
    hitung_huruf = len(string)
    listhuruf = []
    huruf = ""
    for i in range(hitung_huruf):
        huruf = string[i]
        if huruf == 'A' or huruf =='a' or huruf == 'I' or huruf =='i' or huruf == 'U' or huruf =='u' or huruf == 'E' or huruf =='e' or huruf == 'O' or huruf =='o':
            listhuruf.append("*")
        else:
            listhuruf.append(huruf)
    listhuruf1 = ""
    for i in range(hitung_huruf):
        listhuruf1 = listhuruf1 + listhuruf[i]
    return listhuruf1

print(ganti_vokal("Cat"))