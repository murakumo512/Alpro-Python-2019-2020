import re
txt = "The rain in Spain"

x = re.findall("\S", txt)
print(x)