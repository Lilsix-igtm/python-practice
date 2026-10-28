#Learning how to use string in print statement

print('exaple')
name = input('What is your name?')
print('Hello')
print(name)

print('Hello \nworld')

print('adding')
x = 532 + 12
print(x)
y = x / 2
print(y)
print('yay i did math')


first_name = 'Emezuo'
last_name = 'Ejidike'
print(first_name + ' ' + 'Hello' + ' ' + last_name)

sentence = 'The dog is named Sammy'
print(sentence.upper())
# THE DOG IS NAMED SAMMY

print(sentence.lower())
# the dog is named sammy

print(sentence.capitalize())
# The dog is named sammy

print(sentence.count('a'))

print(sentence.count('b'))


first = input('what is your name?')
last = input('What is your surname?')

output = 'Hello,' + first.upper() + ' ' + last.upper()
output = 'Hello {} {}' .format(first, last)
output = 'Hello {1} {0}' .format(first_name, last_name)
output = f'Hello, bro {first} \n{last}'
print(output )


#Learning Numbers



first_num = input('What is your age?')
second_num = input('What year are you born?')
name = 'Emezuo'
output = (int(first_num) + int(second_num))
output_w = (float(first_num) + float(second_num))
print(output_w)
print (output)
print(first_num + second_num)
answer = f'Hello, {name} I am {first_num} years old. I was born in {second_num}'
print(answer)

day_in_february = 29
print(str(day_in_february) + 'days in february')
print(first_num + second_num)

# print(first_num * second_num) this wont work cuz number in input is now treated as string so we need to convert it to int or float

print(int(first_num) * int(second_num))
print(int(first_num) ** int(second_num))


#   Dates:
 
#To import current date and time we need to use from datetime Library
from datetime import datetime, timedelta

#returns current date
current_date = datetime.now()

#convert date to string when concatenating with string
output = f'Today is? {current_date}' 
print('Today is?' +' ' + str(current_date))
print(output)


#using timedelta gotten from datetime library for tracking a period of time
period = timedelta(days=1)
yesterday = current_date - period
output_u = f'Yesterday was {yesterday}'
print('Yesterday was' + ' ' + str(yesterday))
print(output_u)

week_ago = timedelta(weeks=1)
last_week = current_date - week_ago
previous_week = f'Last week was: {last_week}'
print(previous_week)

#used to track the exact part u want to display
print(current_date.day)
print(current_date.hour)
print(current_date.minute)
print(current_date.month)

#converting from string to date
birthday = input('When is your birthday (dd/mm/yy)?').strip()

# strptime converts string to date format meaning "string parse time"
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

# strftime converts date back-to string format meaning "string format time"
display_date = f'Birthday {birthday_date.strftime("%d/%m/%Y")}'
print(display_date)



