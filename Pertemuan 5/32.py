def cetak_maksimal(a, b):
    if a > b:
        print("%s merupakan nilai maksimal" % a)
    elif a == b:
        print("%s sama dengan %s" % (a, b))
    else:
        print ("%s merupakan nilai maksimal" % b)
cetak_maksimal(10, 100)


def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

#print (faktorial(10))