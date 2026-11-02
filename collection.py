#Dictionary

christopher = {}
christopher ['first'] = 'christopher'
christopher ['last'] = 'Harrison'

susan = {}
susan ['first'] = 'Susan'
susan ['last'] = 'Ibach'

#putting dictionary inside a list
people = []
people.append(christopher)  
people.append(susan)
people.append({
    'first': 'Bill', 'Last': 'Gates'
})

print(len(people))
print(people)

names = ['Chioma', 'Ifeoma', 'Marcel', 3, 8, 20]
names.append(people)
names.append(christopher)
print(len(names))
print(names[0:4])
print(names[2:6])
print(names[1])
print(names)

#finding where the values are using index

print(names.index('Ifeoma'))

where_is = 'Marcel'

if where_is in names:
    position = names.index('Marcel')
    pos = f'{where_is} is in {position}'
else:
    pos = f'{where_is} was not found'
print(pos)

