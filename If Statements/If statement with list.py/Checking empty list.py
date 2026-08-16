# Checking that a list is not empty-
# For checking if the list contains any items. An emptu list is treated as "False"
# Syntax- if requested_toppings:


requested_toppings = []
if requested_toppings:
  for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
  print("\nFinished making your pizza.")
else:
  print("Are you sure you want a plain pizza?")
  