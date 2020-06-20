def ganjil(b):
  if b==1:
    print(b)
    return b
  else:
    if b % 2 != 0 :
      print(b)
      return b + ganjil(b-1)
    else:
      return ganjil(b-1)
      
print(ganjil(10))