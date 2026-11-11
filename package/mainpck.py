from modules.greetings import say_hello, say_goodbye
from modules.calculation import add, subtract, multiply

say_hello('Hello, welcome to the program!')
say_goodbye()
say_hello('This is a warning message.', warning=True)

first_num = 10
second_num =15

result = add(first_num, second_num)

result1 = subtract(first_num, second_num)

result2 = multiply(first_num, second_num)

print(f'Result equals: {result}')
print(f'Result1 equals: {result1}')
print(f'Result2 equals: {result2}')

