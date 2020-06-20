def myfunc():
    print("A")
    yourfunc()

def yourfunc():
    print("B")

for i in range(6):
    if i == 1:
        yourfunc()
        func = yourfunc
    elif i > 4:
        func()
        func = myfunc