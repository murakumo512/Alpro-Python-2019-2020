with open("lorem.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
f = open("lorem.txt", "w+")

for i in range(3):
    f.write("Baris ke-%d\n"%(i))
f.close()
