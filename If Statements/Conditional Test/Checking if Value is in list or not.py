#  Checkig Whether a Value is in a List-
# >Sometimes it's important to check whether a list contains a certain value before taking an action. To find out whether a particular value is already in a list usse the keyword 'in'.

#  Checking Whether a Value is not in a list-
# >Other times, it's important to know if a value does not appear in a list. For these conditions, you can check whether a value is in the list by allowing the person to submit a comment.
banned_person = ['kamal','caroline','Nisha']
person = 'maria'
if person not in banned_person:
  print(person.title()+", you can post a reponse if you wish")

