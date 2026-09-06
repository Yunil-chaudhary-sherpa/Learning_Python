'''Using Flags-
For a program that should run only as long as many conditions are true, a flag is used. This variable determines whether or not the entire program is active.
'''
prompt = "\nTell me something, and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program."
active = True       # Flag
while active:
  message = input(prompt)
  if message == 'quit':
    active = False
  else:
    print(message)
