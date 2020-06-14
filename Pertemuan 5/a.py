for row in range(0,7):
    for column in range(2,6):
        if column >=6 or(row==4 or row==3 or row==2) and (row>5 or column>0):
            print("*",end="")
            print()