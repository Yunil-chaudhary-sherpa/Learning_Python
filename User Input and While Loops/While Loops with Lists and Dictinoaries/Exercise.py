'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''
sandwich_orders = ['tuna sandwich','salami sandwich','beef sandwich','chicken sandwich','veg sandwich','cheese sandwich']
finished_sandwich = []
while sandwich_orders:
  sandwich = sandwich_orders[0]
  sandwich_orders.remove(sandwich)
  finished_sandwich.append(sandwich)
  print(sandwich.title()+" is ready to serve.")
print("\nTotal Sandwiches: ")
for sandwich in finished_sandwich:
  print(sandwich)

'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich'''
sandwich_orders = ['tuna sandwich','pastrami sandwich','salami sandwich','beef sandwich','pastrami sandwich','chicken sandwich','veg sandwich','pastrami sandwich','cheese sandwich']
finished_sandwich = []
print("Pastrami Sandwiches are out of stock.")
while 'pastrami sandwich' in sandwich_orders:
  sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
  sandwich = sandwich_orders[0]
  sandwich_orders.remove(sandwich)
  finished_sandwich.append(sandwich)
  print(sandwich.title()+" is ready to serve.")
print("\nTotal Sandwiches: ")
for sandwich in finished_sandwich:
  print(sandwich)

'''Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world where would you go? Include a block of code that prints the results of the poll.'''
Places = {}
poll_active = True
while poll_active:
  name = input("\nEnter your name: ")
  dream_visit = input("\nIf you could visit one place in the world where would you go?")
  Places[name] = dream_visit
  repeat = input("\nAnymore response (yes/no): ")
  if repeat == 'no':
    poll_active = False
print("\n---Final Poll---")
for name, dream_visit in Places.items():
  print(name+"'s dream destination is "+dream_visit+'.')