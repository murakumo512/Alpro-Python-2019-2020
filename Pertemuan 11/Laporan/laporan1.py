dictionary_days = dict() # dictionary baru
qq=dict()
qqa=""
www=[]
domain=""
#fname = input('Enter a file name: ')
fname="mbox-short.txt"
try:
 fhand = open(fname)
except FileNotFoundError:
 print('File cannot be opened:', fname)
 exit()
j=0
for line in fhand:
  words = line.split()
  #print(words)
  if (len(words) < 3 or words[0] != 'From:') and (len(words) < 3 or words[0] != 'To:') :
    continue
  else:
    if words[2] not in dictionary_days:
      dictionary_days[words[2]] = 1 # pertama    
      qqa=words[2]
      x = qqa.find("@")
      domain=qqa[x:len(qqa)-1]
      www.append(domain)  #masukan ke list
    else:
      dictionary_days[words[2]] += 1 # +1
      qqa=words[2]
      x = qqa.find("@")
      domain=qqa[x:len(qqa)-1]
      www.append(domain) #masukan ke list
print("email : \n", dictionary_days)
print()
# bagian ini untuk cetak domain
counts=dict()
for word in www:
  if word not in counts:
    counts[word] = 1
  else:
    counts[word] += 1
print("Domain : \n", counts)