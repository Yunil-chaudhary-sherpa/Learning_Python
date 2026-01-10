# Make a list of people you want to invite for dinner and print a message to each of the people.
Invitation_list = ['darey','votey','bam','bipin']
print("I'm having a party soon "+Invitation_list[0].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[1].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[2].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[3].title()+". How about crashing out at my place?")

# As one of the member can't come to party add a statement who can't appear to the party and modify your list replacing it with a new friend then print a message with their in it.
Party_pooper = Invitation_list.pop(3)
print('\n'+"'"+Party_pooper.title()+"'"+" won't be appearing in the party")
Invitation_list.append("Motey")
print("I'm having a party soon "+Invitation_list[0].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[1].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[2].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[3].title()+". How about crashing out at my place?")

# You found a bigger table so add 3 more people you want to invite.
print('\n'+"I found a bigger and I'm inviting three more men "+Invitation_list[0])
print("I found a bigger and I'm inviting three more men "+Invitation_list[1])
print("I found a bigger and I'm inviting three more men "+Invitation_list[2])
print("I found a bigger and I'm inviting three more men "+Invitation_list[3])
Invitation_list.insert(0, 'Banshi')
Invitation_list.insert(3, 'Limbu')
Invitation_list.insert(6, 'Gucci')
print("\n"+"I'm having a party soon "+Invitation_list[0].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[1].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[2].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[3].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[4].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[5].title()+". How about crashing out at my place?")
print("I'm having a party soon "+Invitation_list[6].title()+". How about crashing out at my place?")

# The table you found came out to be unavailable that day so you have to use pop() method to remove all the people until 3 remain and say they are still invited then remove them as well with del() method and check in the terminal if any person remains.
Removing_members = Invitation_list.pop(0)
print("Really sorry to say but the plan is cancelled "+Removing_members.title())
Removing_members = Invitation_list.pop(2)
print("Really sorry to say but the plan is cancelled "+Removing_members.title())
Removing_members = Invitation_list.pop(3)
print("Really sorry to say but the plan is cancelled "+Removing_members.title())
Removing_members = Invitation_list.pop(3)
print("Really sorry to say but the plan is cancelled "+Removing_members.title())
print("Previous plan got cancelled but your still invited "+Invitation_list[0].title())
print("Previous plan got cancelled but your still invited "+Invitation_list[1].title())
print("Previous plan got cancelled but your still invited "+Invitation_list[2].title())
del Invitation_list[0]
del Invitation_list[0]
del Invitation_list[0]
print(Invitation_list)