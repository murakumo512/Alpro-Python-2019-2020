import re

def ubah(x):
  x = re.split("\s", txt)
  #print(x)
  aa=[]
  for i in range(0,len(x)):
    xa = re.sub(r"A|a", "1", x[i])
    xa = re.sub(r"I|i", "2", xa) 
    xa = re.sub(r"U|u", "3", xa) 
    xa = re.sub(r"E|e", "4", xa) 
    xa = re.sub(r"O|o", "5", xa)
    aa.append(xa)
  print(aa) 

txt = "Mardonius Riel"
ubah(txt)  