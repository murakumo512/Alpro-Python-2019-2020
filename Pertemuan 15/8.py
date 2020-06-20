import re

txt = "Router(config)#hostname R1"
x = re.findall("\W", txt)
print(x)