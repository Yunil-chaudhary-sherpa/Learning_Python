'''A list in a dictionary-
If you want to store multiple typess of information in a single key we can use list in the key.
'''

Hobbies = {'Schmidt':['Spielen Fußball','Hören Musik','lesen buch'],
           'Maria':['Hören Musik'],
           'Peter':['meditation','spielen gitarre']}
for name, hobbies in Hobbies.items():
  print('\n'+name+"'s hobbies:")
  for hobby in hobbies:
    print(hobby)