x = [111,222,333]
tuple = ('Phyton',) * (x.__len__() - x[::-1][0])
print(tuple)