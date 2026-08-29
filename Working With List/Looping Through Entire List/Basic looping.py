#  Looping through a entire list-
# >Performing multiple codes that end up with the same outcome make a program long and repetative. That is way loops are used
# Abroad_Friends = ['Limbu','Avinaya','Divendra']
# for Abroad_Friend in Abroad_Friends:
#   print(Abroad_Friend)
# At line 4 the for loop tells python to store the values of Abroad_Friends to Abroad_Friend one at a time.

# Adding message with looped values-
Abroad_Friends = ['Limbu','Avinaya','Divendra']
for Abroad_Friend in Abroad_Friends:
  print(Abroad_Friend.title()+', I will be trying for a abroad country as well.')
  print('I am going to be very rich '+Abroad_Friend.title()+'.\n')
