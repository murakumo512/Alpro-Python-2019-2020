import re

txt = "Sesi satu Senin Siang"
x = re.search(r"\bS\w+", txt)
print(x.group())