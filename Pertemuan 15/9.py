import re

txt = "Q1!w2@e3$i*9"
x = re.findall("\d", txt)
print(x)