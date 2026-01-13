#  IF-elif else Statement-
# >When testing more then two condition in python.

# Print a msg for people of different ages-
#>Age under 4 is free.
#>Age between age 4 and 18 is $5.
#>Age above 18 is $10.
age = 12
if age < 4:
  print("Admission is free.")
elif age < 18:
  print("Admission fee = $5")
else:
  print("Admission fee = $10")

# Using Multiple elif blocks-

# Provide a 50% discount for age above 65.
age = 79
if age < 4:
  Price = 0
elif age < 17:
  Price = 5
elif age > 65:
  Price = 5
else:
  Price = 10
