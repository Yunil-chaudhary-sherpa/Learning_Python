# Modifying Values in Dictionary-
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
char = {'Height':'174'}
print("The players height is "+char['Height']+'.')
# Modifying the key-
char['Height'] = '183'
print("The players height increased to "+char['Height']+'!!!')

# A more complex modification of dictionary-
# Move the player to the right, determine how far to move the player based on its speed.
char = {'x-axis':'-78','y-axis':'33132','speed':'slow'}
print("Orginal x-position:"+str(char['x-axis']))
char['speed'] = 'fast'
if char['speed'] == 'very slow':
  x_increment = 5
elif char['speed'] == 'slow':
  x_increment = 10
elif char['speed'] == 'medium':
  x_increment = 15
else:
  x_increment = 20
char['x-axis'] = int(char['x-axis'])+x_increment
print("New x-position:"+str(char['x-axis']))