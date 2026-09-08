'''Moving Items from One List to Another-
Using while loop to move values from one list to another.'''
# Starting with users that need to be verified and an empty list to hold the verified users.
Unknown_users = ['Keshav','Anil','Nikil','Vainkatesh']
Known_Users = []
# Verify the list until there are no more unknown users and move them to the empty list.
while Unknown_users:
  Current_User = Unknown_users.pop()
  print('Verifing User: '+Current_User.title())
  Known_Users.append(Current_User)

print("The following users have been verified: ")
for Known_User in Known_Users:
  print(Known_User+' has been verified.')
  