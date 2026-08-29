'''Writing clear prompts-
When using input() function you should include a clear and easy to follow prompt.'''
name = input('Please enter your name: ')
print('Hello, '+name+'!')

# Sometimes you'll want to write a prompt that's longer than one line.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
# You can store in a variable and pass that variable to the input() function that allows to build your prompt over several lines.
