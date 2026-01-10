# Store a name in a variable and print a message.

Person_Name = 'Alexander'
print('Hello, '+Person_Name+' would you like to learn some python?')

# Store a name in a vaiable and print the name in lowercase, uppercase and titlecase

User_ID = 'mark'
print(User_ID.lower())
print(User_ID.upper())
print(User_ID.title())

# Print a quote form a famous author
Author_Name = 'Lewis Carroll'
Authors_quote = "If you don't know where you are going, any road will get you there."
print(Authors_quote +'\nBy ' +Author_Name)

# Store a person's name and make sure uoe use character combination (\t,\n) at least once and print . Then print the name using each of the stripping function (lstrip(), rstrip() and strip())
person_name_1 = '    Sir Isaac Newton'
person_name_2 = '  Albert Einstein  '
person_name_3 = 'Robert Openheimer   '
print("Name's of Famous Scientist:"+ "\n\t"+person_name_1.lstrip()+"\n\t"+person_name_2.strip()+"\n\t"+person_name_3.rstrip())