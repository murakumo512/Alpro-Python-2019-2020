import re

email = input("emailm: ")
a = re.match(r"\S+@\S+", email)
print(a) 
  