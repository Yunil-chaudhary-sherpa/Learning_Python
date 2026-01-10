# User might want to add new elements in the list for many reasons

#  Adding Elements-
# >Adding new values in a list

#1. Appending elements-
# > When appending a new value in the list; the values is added in the end of the line.
Sports_Car = ['Lamborghini','Bugatti','GT-R','Ferrari']
print(Sports_Car)
Sports_Car.append('Porscha')
print(Sports_Car)
# > For building a more dynamic list we a create a empty list then add required values 
Sports_Car = []
Sports_Car.append('Lamborghini')
Sports_Car.append('Bugatti')
Sports_Car.append('GT-R')
Sports_Car.append('Ferrari')
Sports_Car.append('Porscha')
print(Sports_Car)

#2. Inserting Elements-
# > To add values in a list in particular position insert is used
Sport_Car = ['Lamborghini','Bugatti','GT-R','Porscha']
Sport_Car.insert(2,'Ferrari')
print(Sport_Car)