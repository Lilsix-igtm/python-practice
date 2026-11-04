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