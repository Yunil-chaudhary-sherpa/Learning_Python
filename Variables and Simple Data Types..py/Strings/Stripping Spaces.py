# Stripping Whitespace

# rstrip()- strips whitespace from right
ongoing_book = ' Ikigai '
print(ongoing_book.rstrip())

#lstrip()- strips whitespace from left
ongoing_game = ' Horizon-Zero Dawn '
print(ongoing_game.lstrip())

# strip()
future_hobby = '              Bartender Classes          '
print(future_hobby.strip())

# The strip() method only removes the whitespace for the particular print command

# Permanent Strip
future_hobby = '     Bartender Classes   '
future_hobby = future_hobby.strip()
print(future_hobby)