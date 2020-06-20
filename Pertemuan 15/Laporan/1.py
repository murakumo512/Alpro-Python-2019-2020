import re
import datetime
from datetime import date
import random
import string


datetime_str = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."

match = re.findall(r'\d{4}-\d{2}-\d{2}', datetime_str)
# \d digit --> cari angka
# {4} banyaknya digit   

for i in range(0,len(match)):
    date = datetime.datetime.strptime(match[i], '%Y-%m-%d').date()
    tgl2 = date.today()
    selisih = tgl2 - date
    print(date.strftime("%d/%m/%Y"),'Selisih', selisih.days, ' hari')