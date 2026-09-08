'''Removing all instances of specific values from a list-
To remove a specific category of value/s in a list a while loop can simplify repetative task.'''
pets = ['dog','cat','snake','cat','parrot','cat','fish','rabbit']
print(pets)
while 'cat' in pets:
  pets.remove('cat')
print(pets)
