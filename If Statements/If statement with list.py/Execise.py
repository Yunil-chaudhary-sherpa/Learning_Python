'''Make a list of 4 usernames including 'admin'. WAP that print a greeting to users entering the website.
>If 'admin' enters, print a special greeting.
>Otherwise, print a generic greeting.'''
Usernames = ['buch','frau','fragan','admin']
for Username in Usernames:
  if Username == 'admin':
    print("Hello admin, would you like a status report?")
  else:
    print("Hello "+Username+", thank you for visiting the site!!!")

'''Check if the list is not empty-
>If the list is empty, print the message we need to find some users!
>Remove all of the usernames from your list, and make sure the correct message is printed.
'''
usernames = []
if usernames:
  for username in usernames:
    if Username == 'admin':
        print("Hello admin, would you like a status report?")
    else:
        print("Hello "+Username+", thank you for visiting the site!!!")
else:
   print("We need to find more users!")

'''WAP that simulates how websites ensure that everyone ahs a unique username.
>Make a list of 4 username called current_users.
>Make another list called new_users with a least two users.
>Loop to see if every user name has already been used and print "enter new username" if used already, else use successful.'''
current_users = ['anil','nitesh','kamal','bimal']
new_users = ['anil',"Rajesh",'NITESH']
for new_user in new_users:
  if new_user in current_users:
     print("Enter new username.")
  else:
     print("Successfull")

