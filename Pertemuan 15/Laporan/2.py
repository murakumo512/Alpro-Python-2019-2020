import random
import string
import re

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

my_str = """Berikut adalah daftar email dan nama pengguna dari mailing list: 
anton@mail.com dimiliki oleh antonius 
budi@gmail.co.id dimiliki oleh budi anwari 
slamet@getnada.com dimiliki oleh slamet slumut 
matahari@tokopedia.com dimiliki oleh toko matahari 
"""
imail = re.findall(r'[a-zA-Z0-9_.+-]+@', my_str) 
email = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+', my_str)
#match = re.findall(r'[\w\.-]+@[\w\.-]+', my_str) #pake ini juga benar

for i in range(0,len(imail)):
    nama=str(imail[i][0:len(imail[i])-1])
    passw=get_random_alphaNumeric_string(8)

    print(email[i],nama,'Password',passw)