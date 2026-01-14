#  Testing multiple conditions-
# >When checking all the conditions of interest, you should use series of if statements as after the one of the interest is found the python ends the program.
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
  print('Adding Mushrooms.')
if 'pepperoni' in requested_toppings:
  print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
  print('Adding extra cheese.')
print("\nFinished making pizza!")