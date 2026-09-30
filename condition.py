#CONDITIONAL STATEMENTS
#if = do something if it's true
#else= do something else

age = int(input('Enter Your Age:'))

if age >= 18:
  print('signed up ')

elif age < 0:
  print('You haven\'t been born yet') 
else:
  print('you must be 18')  

for_sale = True

if for_sale :
  print('item for sale')
else :
  print('not for sale')  

name = input('Enter your name:')  

if name == "":
  print('you must type your name')
else:
  print(f'hello {name}')  


score = int(input('Enter your score:'))

if score >=80:
  print('Grade A')
elif score >= 70:
  print('Grade B')
elif score >= 60:
  print('Grade C')
elif score >= 50:
  print('Grade D')   
else :
  print('Grade F')     


#  #  CHECKING EVEN AND ODD NUMBERS
number01 = int(input('Enter a number:'))

if number01 % 2 == 0:
  print('This is an even number')
else:
  print('This is an odd number') 

#USING AND
age = 25

if age>= 13 and age <= 17:
  print('You are a teenager')
else:
  print('Non teenager')

# Using OR
day = 'Saturday'

if day == 'Saturday' or 'Sunday':
  print('it\'s weekend')

# using NOT
#NOT operator reverses a condition
logged_in = False

if not logged_in:
  print('Please log in.')

# PRATICAL EXAMPLES
# 
# LOGIN SYSTEM
username = input('Enter username: ')
password = input('Enter password')

if username == 'admin' and password == '1234':
  print('login sucessful.')
else:
  print('invalid username or password')

# ATM WITHDRAWAL
balance = 50000
amount = int(input('Enter withdrawal amount'))  

if amount <= balance:
  print('Withdrawal sucessful.')
  print('Remaining balance:', balance - amount)
else:
  print('Insufficient funds.')

# Simple calculator with conditions
number1 = float(input('Enter first number:'))    
number2 = float(input('Enter second number:'))

operator = input('Enter operator(+, -, *, /):')

if operator == '+':
  print('Answer:', number1 + number2)

elif operator == '-':
  print('Answer:', number1 - number2)

elif operator == '*':
  print('Answer:', number1 * number2)

elif operator == '/':
  print('Answer:', number1 / number2) 

else :
  print('Invalid operator')     

