# While writing a program the user moght remove a set or a item from the list

#  Removing Elements-
# >Removing values from a list

#1. Del Statement-
#  >If you know the position of the elements to remove from the list del statement is used.
Metallic_bands = ["Slipknot","SOAD","Pantera","Deftones",'ACDC']
print(Metallic_bands)
del Metallic_bands[4]
print(Metallic_bands)

#2. Pop() method-
#  >This method removes the last item in a list, but it lets you work with that item after removing.
Metallic_bands = ["Alice in Chains","Avenged Sevenfold","KoRn","CheVelle","My Chemical Romance","Disturbed","Lamp Bizkit","Nirvana","Trivium","Linkin Park"]
print(Metallic_bands)
Popped_Metallic_bands = Metallic_bands.pop(4)
print(Metallic_bands)
print(Popped_Metallic_bands)

# Using the pop() method with previous chapter
Metallic_bands = ["Alice in Chains","Avenged Sevenfold","KoRn","CheVelle","My Chemical Romance","Disturbed","Lamp Bizkit","Nirvana","Trivium","Linkin Park"]
Correction = Metallic_bands.pop(4)
print("'"+Correction+"'"+ 'is not a metallic band.')
# After a value is popped; the item will not be stored in a list

#3. Removing an item by value-
#  >If the position of the value is not known and the value has to be removed this method is used.
Traveling_trips = ['Manang','Mustang','Pokhara','Chitwan','Solukhumbu','Barasinghe']
Traveling_trips.remove('Solukhumbu')
print(Traveling_trips)

# User can also remove a value popped from a list.
Traveling_trips = ['Manang','Mustang','Pokhara','Chitwan','Solukhumbu','Barasinghe']
print(Traveling_trips)
Least_Important = 'Solukhumbu'
Traveling_trips.remove(Least_Important)
print(Traveling_trips)
print("\n"+Least_Important.title()+' is least important trip i want to visit.')