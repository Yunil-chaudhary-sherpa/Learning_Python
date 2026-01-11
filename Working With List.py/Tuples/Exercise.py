# Use a for loop to print names of food provided by a restaurant offers in a tuple. Modify one of the item from tuple and make sure that python rejects the change.
Hotel_Purnimas = ('Sukha Roti','Rice','Sabji','Salad','Naan')
print("Foods offered by Hotel Purnima:")
for Hotel_Purnima in Hotel_Purnimas:
  print('\t'+Hotel_Purnima)
Hotel_Purnimas.append('Momo')
print(Hotel_Purnimas)

# The menu is improvised by changing to items in the menu change the value in tuple and print using for loop.
Hotel_Purnimas = ['Pizza','Momo','Naan','Sabji','Salad']
print('The revised menu of Hotel Purnima:')
for Hotel_Purnima in Hotel_Purnimas:
  print('\t'+Hotel_Purnima)