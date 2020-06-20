def func1(yeay):
    idx = len(yeay) -1
    yeay2 = str()
    while idx >= 0:
        yeay2 += yeay[idx]
        idx -= 1
    return yeay2

def func2(yeay):
    idx = 0
    yeay2 = str()
    while idx < len(yeay):
        yeay2 += yeay[idx]
        idx += 1
    return yeay2

text = 'Thisnis not the matter you can do it or not'
text2 = 'Asuuuuuuuuuuuuu dasdasd asd a'
print(func1(text), func2(text))