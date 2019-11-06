hello = 'hello, world!'
python = 'Python3'
str_1 = "It's Just a Flesh Wound"
str_2 = 'We Are The Knights Who Say Ni Ni'
str_3 = "Let's Not Go To Camelot. 'Tis a Silly Place"

name = 'John'
age = 20

# Concatenate
print('My name is ' + name + ' and I am ' + str(age))

# Format Positioning ( < 3.6 )
print('My name is {name} and I am {age}'.format(name=name, age=age))
# print('My name is {} and I am {}'.format(name, age))

# F-Strings (^3.6)
# print(f'My name is {name} and I am {age}')

print('\n')
print(hello)

# Sub String
print(hello[0:5])

# Lenght
print('str_1 Tem {} letras...'.format(len(str_1)))

# Split
print(str_2.split())  # Default Delimiter is " " (space)
print(str_2.split('Ni'))  # Delimiter defined as 'Ni'

# Replace
print(str_2.replace('Ni', 'Ekki-ekki-ekki-ekki-ptang'))
print(python.replace('3', '^3.5'))

# Find position
print(str_2.find('Ni'))

# Count
print(str_2.count('Ni'))

# Upper, Lower, Capitalize
print(python.upper())
print(python.lower())
print(hello.capitalize())

# Is all alphanumeric
print(hello.isalnum())

# Is all alphabetic
print(hello.isalpha())

# Is all numeric
print(hello.isnumeric())

print('\n')
