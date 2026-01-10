# Use a for loop to print numbers from 1 to 20.
for value in range(1,21):
  print(value)

# make list from 1 to 1000000 and then use a for loop to print the numbers.
Numbers = list(range(1,1000001))
for number in Numbers:
  print(number)

# Make a list of numbers from 1 to 1000000 then use min() and max() to make sure pyhton actucally starts a 1 and ends at 1000000 and use sum() to see ho fast python print the sum.
Numbers = list(range(1,1000001))
print('Minimum Number',min(Numbers))
print('Maximum Number',max(Numbers))
print('Sum of numbers:',sum(Numbers))

# Print odd numbers from 1-20.
for value in range(1,20,2):
  print(value)

# Make a list of multiples of 3 from 3 to 30.
Multiples = list(range(3,31,3))
for Multiple in Multiples:
  print(Multiple)

# Make a list of cubes from 1 to 10.
Cubes = list(range(1,10))
for value in Cubes:
  Cube = value**3
  print(Cube)

# Make a cube comprehensinon.
Cubes = [value**3 for value in range(1,10)]
print(Cubes)
