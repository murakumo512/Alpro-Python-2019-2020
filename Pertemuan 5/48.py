def zig(x):
    print("Zag"*x,end = '')
print("zig",end='')
def zag(x):
    print("zig"*x,end='')
    zig(x-1)

zig(2)
zag(2)