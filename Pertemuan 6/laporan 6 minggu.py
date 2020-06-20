#! $HOME/bin/python
# program python 23/12/2017 by Hendriyawan
# mencari bilangan prima :
# 1. banyaknya bilangan prima
# 2. bilangan prima terbesar
# 3. bilangan prima terkecil


#soal 1
#fungsi untuk menecek apakah bilangan prima
def cekprima(num):
	if num < 2:
		return False #mengembalikan nilai False jika nomer lebih kecil 2
	for prime in range(2, num):
		if num % prime == 0: #jika angka hasil bagi nilai prime == 0, maka mengembalikan nilai False, karena bukan bilangan prima
			return False
	return True
	
#fungai mencari bilangan prima dari 1 - maksimal nomer yang di masukan
def find_primes(max_num):
	primes = [] #bilangan prima akan di tampung di list ini
	for prime in range(0, max_num):
		if cekprima(prime):
			primes.append(prime)
			
	total_primes = str(len(primes)) #total bilangan prima
	largest_prime = str(primes[-1]) #bilangan prima terbesar
	smallest_prime = str(primes[0]) #bilangan prima terkecil
	print('bilangan prima terbesar : %s' % (largest_prime))
	

max = int(input('masukan nilai : '))
find_primes(max)




def soal2(n):
    for i in reversed(range(n)):
        for j in range(1, i+1):
            print(j, end=' ')
            i+=1
        print() 

n = int(input("Masukkan bilangan : "))
soal2(n)




#def soal3(tinggi, lebar):
#    for i in range(tinggi, lebar):
#        print('*'*10)


#tinggi = int(input("Masukkan tinggi :"))
#lebar = int(input("Masukkan lebar : "))
#soal3(tinggi, lebar)
