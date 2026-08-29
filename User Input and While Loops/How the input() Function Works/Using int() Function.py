'''Using int() function to accept numerical inputs-
Python interprets everything the user enters as string. So int() function is used to create integer values.
'''
height = int(input('Enter your height in centemetres: '))
if height >= 100:
  print("Welcome to the basketball team!!")
else:
  print("Sorry, you are not tall enough.")