import re

txt = "The rain in spain"
x = re.findall("[a-m]+", txt)
print(x[3])