dictionary_days = dict() # dictionary baru
#fname = input('Enter a file name: ')
fname="mbox-short.txt"
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
  words = line.split()
  #print(words)

  if len(words) < 3 or words[0] != 'From':
    continue #jika awal bukan kata "from"
  else:
    kk=""
    kk=words[5] #masukan dulu ke string
    kk=(kk[0:2]) #ambil 2 huruf dari jam
    if kk not in dictionary_days: #cek apakk ada di dict
      dictionary_days[kk] = 1 # pertama
    else:
      dictionary_days[kk] += 1 # +1

print(dictionary_days)
for key, val in list(dictionary_days.items()):
 print(key,val)