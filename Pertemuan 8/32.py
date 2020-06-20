def count(a,b):
    sum = int()
    for i in range(len(a)):
        if b == a[i].lower():
            sum += 1
    return sum
    
text = 'This is not the matter you can do it or not'
text2 = 'This is about you want to do it or not'
task = 'a'
print(count(text, task) + count(text2, task))