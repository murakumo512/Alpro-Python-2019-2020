import re

txt = "Bermain Bersamamu Hari Ini"
tmp = len(txt)
for x in range(tmp):
    txt = re.sub("[aie]","1", txt)
new = re.findall("\d",txt)
print(len(new))