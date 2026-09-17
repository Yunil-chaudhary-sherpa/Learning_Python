'''Arguments and Parameters-
In the preceding greet_user() function, we defined greet_user() to require a value for the variable username. Once we called the function and gave it the information (a person’s name), it printed the right greeting. The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job. The value 'kim' in greet_user('kim') is an example of an argument. An argument is a piece of information that is passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses. In this case the argument 'kim' was passed to the function greet_user(), and the value was stored in the parameter username.'''
def greet_user(username):
  '''Display a simple greeting.'''
  print('Hello, '+username.title()+'!')
greet_user('kim')