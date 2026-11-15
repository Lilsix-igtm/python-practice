from manager.grades import calculate_average, check_result

math = int(input('Whats your math score? '))
english = int(input('Whats your English score? '))
crs = int(input('Whats your Crs score? '))

average = calculate_average(math, english, crs)

check_result(average)

from manager.student import student_details, student_age

name = input('Whats your name? ')
age = input('Whats your age? ')

student_details(name)
student_age(age)