#sort
cars = [300,250,50,450,10,75]
cars.sort(reverse=True)
print(cars[0:3])
for i in range (0,3):
	print(cars[i],end=' ')

print()




#append
datax=[]
done= "false"
while done == "false":
  data=input("masukan angka :")
  if data.upper() == "DONE":
    done="true"
  else:
    datax.append(data)
print(datax)
print("nilai terendah:",min(datax))
print("nilai tertinggi:",max(datax))
print()

#open and read the file after the appending:
f = open("t.txt", "r")
txt=f.read() #masukan dalam var
aa=""
txt1=""
x = txt.split()
for i in range (0,len(x)) :
  aa =  x[i]
  ab = "." in aa
  if ab==True:    
    aa=aa[0:len(aa)-1]
  txt1=txt1+" "+aa
xx=txt1.split()
print ("========ISI BERITA========",txt)
print()
print()
print("===========Kata Unik pada Berita========",xx)


