#  Omitting The else block-
# >Sometimes python doesn't need a else block at the end of an if-elif chain.
age = 44
if age < 4:
  Price = 0
elif age < 17:
  Price = 5
elif age > 65:
  Price = 5
elif age <= 65:
  Price = 10
print("Your admission cost is $"+str(Price)+".")