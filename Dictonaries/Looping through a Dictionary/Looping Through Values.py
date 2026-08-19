'''Looping through all values in dictionary-
If you want to output values in dictionary, you can use the values() method to return a list of values without any keys.'''
fav_Lang = {
  'Maria':'python',
  'Jen':'java',
  'Gene':'C',
  'Ali':'C++',
  'Jena':'python'
}
print("The following languages have been mentioned:")
for languages in fav_Lang.values():
  print(languages)
# To see all the values without repetitions set() function is used.
print("The following languages have been mentioned:")
for languages in set(fav_Lang.values()):
  print(languages)