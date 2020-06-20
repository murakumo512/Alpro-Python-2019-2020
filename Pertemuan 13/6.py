msg = set([0,5,4,8,3,9])
m = set([1,23,654,27,89,12])

msg = m.copy()
m.clear()
m.add(45)
print(msg)
m.discard(4)
print(sorted(msg),reverse = True)