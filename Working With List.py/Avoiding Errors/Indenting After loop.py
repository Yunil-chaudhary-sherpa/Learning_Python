#  Indenting unecessary after the loop-
# >If you accidentally indent code that should run after a loop has finished; python will not a error but the result won't be as needed.
foods = ['pizza','burger','momo']
for food in foods:
  print(food+' is delicious.')
  print(food+' is bad if consumed daily.\n')

  print('Thank you for the food.')