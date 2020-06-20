import re

txt = "Mardonius Riel"
x = re.findall("[aiueoAIUEO]", txt)
if(x):
    x = re.sub("[aiueoAIUEO]", "1", txt)
else:
    x = re.split("\s",txt)

print(x)