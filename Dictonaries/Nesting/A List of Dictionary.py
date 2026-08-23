'''A list of dicitonary-
Create multiple dictionaries and stores those dictionaries in a single list.'''
Char_1 = {'username':'baleba','rating':'83'}
Char_2 = {'username':'fofana','rating':'79'}
Char_3 = {'username':'acuna','rating':'75'}
Characters = [Char_1,Char_2,Char_3]
for char in Characters:
  print(char)

# Making a list of characters-
Characters = []
for char_numbers in range(30):
  new_char = {'username':'enter','rating':'not calculated','age':'enter'}
  Characters.append(new_char)
for char in Characters[0:5]:
  print(char)
print('...')
print("The total number of characters:"+str(len(Characters)))
for char in Characters[3:5]:
  if char['username'] == 'enter':
    char['username'] = 'diomande'
    char['age'] = '16'
    char['rating'] = '65'
for char in Characters[0:5]:
  print(char)