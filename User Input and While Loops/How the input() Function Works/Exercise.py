# WAP that asks the user what kind of rental car they would like. Print a message about that car.
Car = input("Enter the car name: ")
print("Searching for "+Car+'...')

# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
Member_Num = int(input("Enter the number of people in the group: "))
if Member_Num < 8:
  print("Please wait for a table to clear.")
else:
  print("The table is ready!")

# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
Num = int(input("Enter a number: "))
if Num % 10 == 0:
  print("Number is the multiple of 10.")
else:
  print("Number is not the multiple of 10.")
