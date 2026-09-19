'''Positional Arguments- 
When calling a function, Python must watch argument in the function call with a parameter in the function definition  The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.
'''
def user_info(username,gender):
  print("\nMy name is "+username.title()+'.')
  print("\nMy gender is "+gender+'.')
user_info('yunil','male')
# Multiple arguments
user_info('kamal','male')
user_info('anu','female')
# Note- Order of arguments matter in postional arguments.