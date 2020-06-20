def removespace(string): 
    string=string.replace(".","")
    string=string.replace(" ", "")
    string=string.replace(",", "")
    return string

def caka(string):
  fname=string
  try:
    fhand = open(fname)
  except:
    print('File cannot be opened:', fname)
    exit()
  counts = dict()
  for line in fhand:
    words = line.split()
    for word in words:
      kat=removespace(word)
      kat=kat.lower()
      if kat not in counts:
        counts[kat] = 1
      else:
        counts[kat] += 1

#print(counts)
    for t in counts:
      print("kata ",t,"ada",counts[t])

#masukan ke sets
    txt1set=set()
    for t in counts:
      txt1set.add(t)
    print(txt1set)
    return txt1set
#-----------------------------------
def ffname(string):
  fname = input("file name "+string+":")
  return fname

def intersek(set1,set2):
  inter=set1&set2
  return inter

filename=dict()
for i in range(0,2):
  sss=str(i)
  mm=ffname(sss)
  filename[i]=mm
hh=dict()
for i in filename:
  hasil=caka(filename[i])
  hh[i]=hasil
print("hhh:",hh)
for i in range(1,len(hh)):
  gg=hh[i-1]&hh[i]
print("intersek cara for :",gg)

print("intersek cara manual:",intersek(hh[0],hh[1]))