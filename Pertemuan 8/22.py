fungsi = open("1.txt", "r")

f1 = fungsi.readline(11)
print(f1)

def file(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print(file("1.txt"))