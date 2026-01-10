# Make a long list and print the first three, three from middle and last three items from the list.
House_Items = ['Bed','Sofa','TV','Table','Locker','Stove','Curtains','Basin','Shoe Rack','Oven','Cooker','Bulb']
print("First three items:")
print(House_Items[:3])
print("\nMiddle three items:")
print(House_Items[3:6])
print("\nLast three items:")
print(House_Items[-3:])

# Exercise 4.1 updatted.
my_pizza = ['pepperoni','chicken','cheese','BBQ','mushroom','hawaiian','paneer']
friend_pizza = my_pizza[:]
my_pizza.append('meat lover')
friend_pizza.append('mexican')
print('My favourite pizzas are:')
print(my_pizza)
print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizza[:]:
  print(pizza)
