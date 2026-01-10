#  Copying a list-
# >To copy a list user must omit first ad last index ([:]).
my_food = ['Laphing','Kima noodle','momo']
Friends_food = my_food[2:]
my_food.append('Pizza')
Friends_food.append('Burger')
print('I prefer '+my_food[3])
print('My friend prefers '+Friends_food[1])
# We use slice to copy a list as if we had set two list in equals it would mean connecting the list and we would have used the append function to add items in the same list.
