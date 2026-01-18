# Checking for special items-

# Using if statements and loop creating a pizza with a specific topping out of stock.
requested_toppings = ['mushroom','olive','cheese','pepperoni']
for requested_topping in requested_toppings:
  if requested_topping == 'olive':
    print('Topping is out of stock.')
  else:
    print("Adding "+requested_topping+'.')
print("\nPizza ready to serve.")
