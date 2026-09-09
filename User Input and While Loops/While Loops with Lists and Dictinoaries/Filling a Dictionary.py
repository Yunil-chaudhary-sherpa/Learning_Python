'''Filling a dictionary with user input-
You can prompt for as much input as you need in each pass through a while loop.
'''
responses = {}
# Set a flag to indicate that polling is active.
poll_active = True
while poll_active:
  name = input("Enter your name: ")
  gender = input("Enter your gender: ")
  # Storing response in dictionary.
  responses[name] = gender
  # Taking more than one response.
  repeat = input("Anymore responses?(yes/no): ")
  if repeat == 'no':
    poll_active = False
print("\n---Point Results---")
for name, response in responses.items():
  print(name+"'s gender is "+response+'.')
print(responses)