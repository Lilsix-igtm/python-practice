# we define a function by using def

from datetime import datetime

#function to print current date and time
def print_time ():
    print('task completed')
    print(datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
print_time()


#writing functions using parameters that will cutomise the data in it
def func_name(param):
    print(param)
    print(datetime.now())

name = 'Marcel'
func_name('Task completed')

for y in range(0,10):
    print()
    func_name('Completed')


# this function will return the first initial of a name
#the return tag is used give back a value from the function

def initial(name_param):
    get_initial = name_param[0:1]
    return get_initial


first_afa = input('What is your first name?').strip()
first_initial = initial(first_afa)


middle_name = input('What is your Middle name?').strip()
middle_initial =  initial(middle_name)

last_name = input('What is your Last name?').strip()
last_initial = initial(last_name)


for z in range(3):
    print(f'Your initials are: {first_initial} {initial(middle_name)} {last_initial}')
    
   

print(f'Your initials are: {initial(first_afa)} {initial(middle_name)}')


#function to add two numbers together

def add_number(a,b):
    return a + b

first_number = int(input('What is your exam score?'))
second_number = int(input('What is your test score?'))

total = add_number(first_number,second_number)
print(f'Your total score is {total}')

learning more of Parameter in functions
def the_initial(named, force_uppercase):
    if force_uppercase:
        initial = named[0:1].upper()
    else:
        initial = named[0:1]
    return initial


name1 = input('Enter first name:').strip()
name1_initial = the_initial(name1, True)

#using named notation
name2 = input('Enter second name:').strip()
name2_initial = the_initial(force_uppercase=False, named=name2)

print(f'your initial is {name1_initial} {name2_initial}')

