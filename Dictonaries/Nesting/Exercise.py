# Make 2 list about info of 2 people and store it in a list (people). Loop through the list and print all the info.
User1 = {'first':'arpit',
         'last':'singh',
         'age':'20'}
User2 = {'first':'sila',
         'last':'malla',
         'age':'21'}
people = [User1,User2]
for person in people:
  print('Name: '+person['first'].title()+' '+person['last'].title())
  print('Age: '+person['age'])

# 