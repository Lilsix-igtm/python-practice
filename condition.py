# learning if else conditions and identation

price = input('Amount paid:').strip()

# price = float(price)
# you cant compare text to number so we need to convert it to float or int
if float(price) >= 2:
   tax = .09
  
else:
   tax = 0
print('Tax added fund:' + ' ' + str(tax))


country = input('What country are you from?').strip()

# country = country.lower()

if country.lower() == 'canada':
   reply = 'Hey u are welcome'
else:
   reply = 'Hey u are not welcome'
print(reply)


#Complex Conditions


#if-elif chain conditions that checks each of ther if the previous fails.
# when theres no else always define ur variable.

province = input('What Province?').strip()
province = province.lower()

if province == 'lagos':
   tax_added = 0.2
elif province == 'anambra':
   tax_added = 2
elif province == 'abuja':
   tax_added = 5
else:
   tax_added = 0
print('Value added tax:' + ' ' + str(tax_added))

# when writing a condition for multiple data to be true then rest 
if province in('anambra', 'abuja', 'lagos'):
   tax_added = 0.9
elif province == 'kwara':
   tax_added = 0.3
else:
   tax_added = 0
print('Value added tax:' + ' ' + str(tax_added))

#nested if statement ie if inside if

continent = input('What continent are you from').strip()
if continent.lower() == 'earth':
    nation = input('What country are you from?').strip()
    if nation.lower() in('canada', 'england', 'ghana', 'usa'):
        caption = 'you are human'
    elif nation.lower() == 'nigeria':
        caption = 'God is your strenght'
    else:
        caption = 'you try sha just make sure no be Nigeria'
else: 
    caption = 'you are not Human'
print(caption)


# complex conditions

# A student makes honour roll if their average is >= 85
# and their lowest grade is not below 70

gpa = float(input('What is your Grade Point Average?').strip())
lowest_grade = float(input('What was your lowest grade?').strip())
country_a = input('What country?').strip().lower()
income = int(input('How much is your income?'))
volunteer_hours = int(input('How many hours?').strip())

if gpa >= 3.5 and lowest_grade >= 70:
   hounour_roll = True
else:
   hounour_roll = False

if country_a == 'canada':
   is_canadian = True
else:
   is_canadian = False

if income < 30000:
   low_income = True
else:
   low_income = False

if volunteer_hours == 100:
   community_leader = True
else:
   community_leader = False


if hounour_roll:
   print('Yes')
else:
   print('No')

if is_canadian:
   print('Yes')
else: 
   print('No')

if low_income:
   print('Yes')
else:
   print('No')

if community_leader:
   print('Yes')
else:
   print('No')

if hounour_roll and low_income:
   print('Result: full scholarship')
elif hounour_roll and community_leader:
   print('Result: Partial Scholarship 50%')
elif hounour_roll and is_canadian:
   print('Canadian Merit - 25%')
else:
   print('No Scholarship try again Next year')

if not hounour_roll and low_income:
   print('Advice: Apply for low income support programme')