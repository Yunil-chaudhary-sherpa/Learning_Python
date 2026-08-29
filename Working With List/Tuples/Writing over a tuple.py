#  Writiing over a tuple-
# >Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple.
dimensions = (190,90,45)
print('Original dimensions:')
for dimension in dimensions:
  print(dimension)
dimensions =(210,105,60)
print("\nModified dimensions:")
for dimension in dimensions:
  print(dimension)
