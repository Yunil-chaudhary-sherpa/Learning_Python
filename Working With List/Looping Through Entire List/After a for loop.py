#  Doing something after a for loop-
# >After summarizing a set of output using a for loop; the user must no indent the next line to tell python that for is not needed.
Places = ['Boudha','Budanilkantha','Swyambhunath','Shantinagar']
Places.sort()
for place in Places:
  print('I have been to '+place.title()+' before.')
  print(place.title()+' is a place of Kathamdu valley.\n')
print("There are also places I haven't been to.")
