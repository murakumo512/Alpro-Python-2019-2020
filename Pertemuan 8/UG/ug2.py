h = eval(input("please enter diamond's height:"))

for i in range(1, h, 2):
    print(" "*(h//2-i//2), "*"*i)
for i in range(h, 0, -2):
    print(" "*(h//2-i//2), "*"*i)