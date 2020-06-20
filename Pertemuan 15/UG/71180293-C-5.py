import re

def pantun(txt1,txt2):
      list1 = re.findall(r".{2}$", txt1)
      list2 = re.findall(r"[a-z]{2}$", txt2)
      if list1 == list2:
            print("Cakepp.. Pantunnya")
      else:
            print("Itu bukan pantun")

txt1 = 'Pohon randu di buat peti'
txt2 = 'Hatiku rindu setengah mati'
pantun(txt1,txt2)