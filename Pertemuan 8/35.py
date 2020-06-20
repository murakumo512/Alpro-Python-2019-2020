text = 'abcdefg'
print(text[:10])


def myfunc(a,b):
    if a > 3:
        return b,a
    else:
        return a,b

swap = myfunc

for i in range(6):
    i,s =swap(i,0)
    print(i)


a = open("lorem1.txt")
b= a.read().split()
c = len(max(b))

print(c)