def func3(a):
    index = a.find(' ')
    text = a[:index + 1] + a[index + 1].upper() + a[index+2:]
    return text

text = 'mika harata'
result = func3(text)
print(result)