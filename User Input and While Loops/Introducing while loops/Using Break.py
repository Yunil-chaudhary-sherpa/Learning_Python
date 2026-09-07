'''Using Breal to exit a loop-
To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, the break statement is used. 
'''
prompt = "\nEnter the name of places visited:"
prompt += "\n(Enter 'quit' when finished.)"
while True:
  city = (prompt)
  if city == 'quit':
    break
  else:
    print(city)