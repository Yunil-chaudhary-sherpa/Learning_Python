'''From the previous exercise copy the dictionary and print the keys and values using loops.
Python_dic = {'.title()':'To capitalize the first letter of a word','.upper()':'To capitalize the whole word','.lower()':'To uncapitalize the whole word'}
for key in Python_dic.keys():
  print(key)
for val in Python_dic.values():
  print(val)
for key_val in Python_dic.items():
  print("Keys:"+key)
  print("Values:"+val)'''

'''Make a dictionary containing three major rivers and the country each river runs through.
>Use a loop to print a sentence about each river.
>Use a loop to print the name of each river included in the dictionary.
>Use a loop to print the name of each country included in the dictionary
'''
Rivers = {"Nile":"Egypt",
          "Bagmati":"Nepal",
          "Ganga":"India"
          }
for river, country in Rivers.items():
  print(river.title()+' runs through '+country.title())
for name in Rivers.keys():
  print(name)
for country in Rivers.values():
  print(country)

