aa =  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
ulang=0
print("Jumlah data: \n:", len(aa))
print("===========================")
for key  in aa:
  ulang=ulang +1
  print(key,aa[key],ulang)

print()


Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']
kamus = dict()
panjang = len(Lista)
for x in range(0,panjang):
  kamus[Lista[x]]=Listb[x]

print("Dictionary = ", kamus)

print()

dictionary_days = dict() # dictionary baru
fname = input('Enter a file name: ')
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
    else:
      dictionary_days[words[2]] += 1 # +1

print(dictionary_days)

print()



