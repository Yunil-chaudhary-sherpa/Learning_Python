'''Looping Through a Dictionary's Keys in Order-
A dictionary only holds connection between a key and its value, but the order is unpredictable. So we can use sorted() function to get the keys in order.
'''
fav_Lang = {
  'Maria':'python',
  'Jen':'java',
  'Gene':'C',
  'Ali':'C++',
  'Jena':'python'
}
for name in sorted(fav_Lang.keys()):
  print(name.title()+", have a nice day.")