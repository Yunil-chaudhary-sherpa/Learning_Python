# Using Multiple Lists-
# Below will be two list to build a pizza, first is a list of available toppings and second is the list of requested toppings.

available_toppings = ['onion','olive','pineapple','extra cheese','mushroom']
requested_toppings = ['mushroom','pepperoni','extra cheese']
for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print("Adding "+requested_topping+".")
  else:
    print("Sorry, "+requested_topping+" is not available!")
print("\nFinished making your pizza.")