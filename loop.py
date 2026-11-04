#for loop

people = ['Christopher', 'Susan']

for name in people:
    print(name)

for i in range(5):
    print(people[i % len(people)])

for nam in range(3):
    print(people[nam])



people.append('Bill')
print(people)


#While loop
index = 0

while index < 7:
    print(people[index % len(people)])
    index = index + 1


password = ''

while password != 'eka123':
    print('wrong password')
    password = input('Enter password:').lower().strip()
    print('checking...\n')

print('you are logged in')


while True:
    passi = input('Password:').lower().strip()

    if passi == 'eka124':
        print('Successfully logged in')
        break
    else:
        print('Wrong password')   

