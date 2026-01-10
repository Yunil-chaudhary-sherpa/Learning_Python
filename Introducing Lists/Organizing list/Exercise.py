# Store the places you want to visit in a list and print it.Then print again with sorted() method and reverse metohd of sorted list.
# Travel_country = ['Japan','Korea','Monaco','Europe','Hawaii']
# print(Travel_country)
# print(sorted(Travel_country))
# print(sorted(Travel_country, reverse=True))
# print(Travel_country)

# # Use reverse() to change the order of the list.
# Travel_country.reverse()
# print(Travel_country)
# Travel_country.reverse()
# print(Travel_country)

# # Use sort() method in the list and print the list then reverse the values in the list print again.
# Travel_country.sort()
# print(Travel_country)
# Travel_country.sort(reverse=True)
# print(Travel_country)

# Create a list of 6 countries you want to visit and print it.
Country = ['Japan','Russia','Monaco','Korea','Germany','UK']
print(Country)

# Remove a country from the list with a message and print it. Then add a new country at the middle and at the end of the list and print the list.
Removed_Country = Country.pop(1)
print('\n'+Removed_Country+" is not the country I'm desperate to visit"+'\n')
Country.insert(3,'France')
Country.insert(7,'Italy')
print(Country)
print()
# Use sorted() method and print the list then reverse the list and print again.
print(sorted(Country)) 
print()
print(Country)
print()
print(sorted(Country, reverse=True))
print()
print(Country)