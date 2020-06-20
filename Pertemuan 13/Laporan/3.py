t = (90,90,90,90)
for i in range (0,len(t)):
  if t[i] in t:
    print(t[i] in t)  # print boolean true/false




tup = ('p','a','n','t','s','u','i','t')
print("ini tuple gan", tup)
str =  ''.join(tup)
print("ini sudah jadi string gan", str)




tuplex = ((2, "x"),(3, "y"))
print("masih tuple gan", tuplex)
print("sudah dalam dict gan", dict((y, x) for x, y in tuplex))



#create a list
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)