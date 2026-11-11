# It tells Python: "Find the module called greetings and make its contents accessible in this file."
import greetings

greetings.say_hello('Hello, welcome to the program!', True)
greetings.say_goodbye()
greetings.say_hello('This is a normal message.')

#This tells python: import the specific function directly from the greetings module.
from greetings import say_hello, say_goodbye

say_hello('Hello, welcome to the program!', True)
say_goodbye()
say_hello('This is a normal message.', False)


#This tells python: import all codes or functions inside the greetings modules. it imports globally all the functions inside the greetings module. This is not recommended because it can cause naming conflicts if there are functions with the same name in different modules.
from greetings import *