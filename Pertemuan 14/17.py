def rekursif(desimal):
    if(desimal > 1):
        rekursif(desimal/2)
    print(int(desimal%2), end = '')
rekursif(10)