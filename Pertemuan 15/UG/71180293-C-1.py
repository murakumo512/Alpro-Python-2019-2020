import re
def passCheck(passwd):
    if re.match('^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&-;_?^])[a-z0-9@$!%*#?&-;_?^]{6,20}$', passwd):
     print("Password valid.")
    else:
      print("Password tidak valid.")
passwd= "MardoniusRiel06*"
passCheck(passwd)