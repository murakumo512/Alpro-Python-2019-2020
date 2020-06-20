my_tuple = (((3,9),2,3,(2,3),5,6,(7,2),8,9,(10,11)))

# converting the tuple to the list
my_list = list(my_tuple)
print (my_list)  # output: [10, 20, 30, 40, 50]


# Here i wanna remove the element "50"
my_list.remove(3) # output: [10, 30, 40]

# again converting the my_list back to my_tuple
my_tuple = tuple(my_list)


print (my_tuple) # output: (10, 30, 40)


tuplex = (((3,9),2,3,(2,3),5,6,(7,2),8,9,(10,11)))
tuplex = list(tuplex)
for x in tuplex:
  if (x == 3):
     tuplex.pop(tuplex.index(x))
tuplex = tuple(tuplex)
print(tuplex)