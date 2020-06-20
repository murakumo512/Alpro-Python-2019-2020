def sum(aa):
    if len(aa) == 1:
        return aa[0]
    else:
        return aa[0] + sum(aa[1:])

print(sum([5,7,3,8,10]))