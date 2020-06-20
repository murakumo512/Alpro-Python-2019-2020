def dicttotuple(data):
    t = list(data.items()) #masukan ke list
    #t.sort()
    tup = tuple(t)
    for i in range (0,len(t)):
        t[i]=[key for key in data.keys()][i],tuple(tup[i][1])
    print(tuple(t))




data = { "Yusta":[90,160], "Elisabeth":[70,177], "Tasya":[50,175]}
dicttotuple(data)




# A simple dictionary
#x = {'X':"yes", 'Y':"no", 'Z':"ok"}

# To print a specific key (for example key at index 1)
#print([key for key in x.keys()][0])