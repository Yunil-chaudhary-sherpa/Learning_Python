'''Looping through all the keys-
The keys() method is useful when you dont need to work with all of the values in a dictionary but  just keys.
'''
fav_Lang = {
  'Maria':'python',
  'Jen':'java',
  'Gene':'C',
  'Ali':'C++',
  'Jena':'python'
}
for name in fav_Lang.keys():
  print(name.title())
# Looping through the keys is actually the default behavior when looping through a dictionary but you can choose to use the keys() method if it makes your code easier to read.
fav_Lang = {
  'Maria':'python',
  'Jen':'java',
  'Gene':'C',
  'Ali':'C++',
  'Jena':'python'
}
friends = {'Maria','Ali'}
for name in fav_Lang.keys():
  print(name)
  if name in friends:
    print('Hi '+name.title()+", so your favorite language is "+fav_Lang[name]+'.')
# You can check is a particular person was in the dictionary or not.
if 'Sara' not in fav_Lang.keys():
  print("Sara wasn't in the list.")
