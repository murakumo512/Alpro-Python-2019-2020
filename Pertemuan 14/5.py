def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
faktorial(10)