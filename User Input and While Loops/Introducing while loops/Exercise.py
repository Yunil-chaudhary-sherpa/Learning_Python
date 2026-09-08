''': Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.'''
prompt = "\nEnter prefered toppings on your pizza: "
prompt += "\n(Enter 'quit' when finished)" 
while True:
  Topping = input(prompt)
  if Topping == 'quit':
    break
  else:
    print("Adding "+Topping+" on your pizza")

'''A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
'''
prompt = "\nEnter your age: "
while True:
  age = input(prompt)
  if age <= 3:
    print("No Charge!")
  elif age>3 and age<= 12:
    print("Your cost is $10.")
  else:
    print("Your cost is $15.")

# Write a loop that never ends, and run it. 
prompt = "\nEnter prefered toppings on your pizza: "
prompt += "\n(Enter 'quit' when finished)" 
flag = True
while flag != False:
  Topping = input(prompt)  
  print("Adding "+Topping+" on your pizza")