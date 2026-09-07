'''Avoiding Infinte Loops-
Every while loop needs to stop running so it won't continue to run forever.
'''
# Finite loop
x = 1
while x <= 5:
  print(x)
  x += 1
# Infinite loop
x = 1
while x <= 5:
  print(x)
# Excluding "x += 1" won't increment "x" causing the loop to be infinte.