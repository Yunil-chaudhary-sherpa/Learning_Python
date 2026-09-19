'''Keyword Arguments- 
In Keyword arguments, you directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion
'''
def describe_pet(animal_type, pet_name):
  print("\nI have a "+animal_type+".")
  print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='kai',animal_type='dog')
