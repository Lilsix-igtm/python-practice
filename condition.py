#learning if else conditions and identation

#price = input('Amount paid:')
#
##price = float(price)
#
#if float(price) >= 2:
#    tax = .09
#   
#else:
#    tax = 0
#print('Tax added fund:' + ' ' + str(tax))
#
#
country = input('What country are you from?')
#
##country = country.lower()
#
#if country.lower().strip() == 'canada':
#    reply = 'Hey u are welcome'
#else:
#    reply = 'Hey u are not welcome'
#print(reply)


#Complex Conditions


#Treating conditions like there are different conditions that has to be checked
# when theres no else always define ur variable.



#province = input('What Province?')
#province = province.lower().strip()
#
#if province == 'lagos':
#    tax_added = 0.2
#elif province == 'anambra':
#    tax_added = 2
#elif province == 'abuja':
#    tax_added = 5
#else:
#    tax_added = 0
#print('Value added tax:' + ' ' + str(tax_added))

#when writing a condition for multiple data to be true then rest 
#if province in('anambra', 'abuja', 'lagos'):
#    tax_added = 0.9
#elif province == 'kwara':
#    tax_added = 0.3
#else:
#    tax_added = 0
#print('Value added tax:' + ' ' + str(tax_added))

#nested if statement ie if inside if

if country.strip().lower() == 'nigeria':
    province = input('What province?')
    if province.lower().strip() in('abuja', 'lagos', 'anambra'):
        tax = 0.3
    elif province.lower().strip() == 'kwara':
        tax = 4
    else:
        tax = 0.9
else:
    tax = 0
output = f'Your tax is: {tax}'
print(output)