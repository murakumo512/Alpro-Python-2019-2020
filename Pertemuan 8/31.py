def func_1(a):
    text = a[0].upper() + a[1:]
    return text

def func_3(c):
    index = c.rfind(' ')
    text = c[:index + 1] + c[index + 1].upper() + c[index+2:]
    return text

text = 'mika harata'
result = func_1(text)
print(result)