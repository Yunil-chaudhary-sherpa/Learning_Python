#  Slicing a list-
# >Selecting a specific amount of value in a list and printing the value seperately.
Players = ['Alex','Charles','Alpha','Clint']
print(Players[1:3])

# If you omit the first index in a slice and print, python will automatically start with index 1 and end at the commanded index.
Food = ['pizza','burger','momo','noodles','pasta']
print(Food[:4])
# It also works vice versa.
print(Food[2:])

# Negative sign indicates any amount of value from the end of the list.
Heroes = ['Batman','Ironman','Superman','Spiderman','Flash']
print(Heroes[-4:])