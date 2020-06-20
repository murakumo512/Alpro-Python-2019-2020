import re

txt = "Menjelang Akhir Tahun Ini"
x = re.search(r"\bT\w+",txt)
print(x.span())