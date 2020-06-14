def myFunc():
    print("a")
    yourFunc()

def yourFunc():
    print("b")

for i in range(6):
    if i == 1:
        yourFunc()
        func = yourFunc
    elif i > 4:
        func()
        func = myFunc