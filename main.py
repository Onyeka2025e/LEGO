print ('Hello World')
# This is a comment

## Mathematical Calculations using variables

num1 = 20
num2 = 5

sum = num1 + num2
difference = num1 - num2
multiply = num1 * num2
divide = num1 / num2

print(num1)
print(num2)
print('Sum:',sum)
print('Difference:',difference)
print('Multiply:', multiply)
print('Divide:' ,divide)

# DATA TYPES
name = 'David'  #strings
age = 20         # integer
height = 1.75    # float
is_student = True  #boolean

# Checking data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#Converting integer to a string
Age = 21
Age_text = str(Age)
print(Age_text)

age1 = 20
print('I am' + str(age1) + 'years old')

print(type(Age))
print(type(Age_text))

#ESCAPE CHARACTERS
topic = 'escape\ncharacter'
print(topic)

info = 'but\tescape'
print(info)

level = 'jsss\b one'
print(level)

#OPTIONAL ARGUMENTS
text = 'apple apple apple'

print(text.replace('apple', 'orange',1))

# PYTHON ARITHMETIC OPERATORS
# // = floor division  (removes decimal places)
# % = modular division (gives you the remainder)
# ** = power 


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
  print(f"hello {name}")  



