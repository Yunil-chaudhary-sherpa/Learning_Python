#  Using the range() function-
for value in range(1,5):
  print(value)
# Although the code looks like it should print numbers from 1 to 5; it doesn't print number 5 due o off-by-one behaviour

#  Using range() to make a list of numbers-
# >If user wants to make a list of numbers , user can wrap a list() function around a range() function.
Number = list(range(1,6))
print(Number)

# We can also use the range() function to tell python to skip number in range.
even_numbers = list(range(2,11,2))
print(even_numbers)

# Making a list of first 10 square numbers.
squares = []
for value in range(1,11):
  square = value**2
  squares.append(square)
print(squares)
  