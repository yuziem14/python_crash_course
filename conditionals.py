# Basic Structure
'''
if <conditional>:
    pass
elif <conditional>:
    pass
else:
    pass
'''
# Logic Expressions (==, !==, >, <, >=, <=)
# Logic Operators (and, or, not, is)

x = 10
y = 10

print('Booleans: ')
print('\t{}'.format(x > y))
print('\t{}'.format(x == y))
print('\t{}'.format(x < y))

print('\nResult: ')
if x > y:
    print('\tX > Y')
elif x == y:
    print('\tX == Y')
else:
    print('\tX < Y')

print('\n')

print('------------ Inputs ------------')
language = input('Language: ').capitalize()
version = input('Version: ')
print('---------------------------------\n')

if language == 'Python' and version == '3.8':
    print('Version 3.8')

if language == 'Java' or language == 'Python':
    print('Python or Java')
elif language == 'Pascal' or language == 'Javascript':
    print('Pascal or Javascript')

if not language == 'C':
    print('Not C')

print('\n')

print('Booleans: ')
print('\t{}'.format(language == 'Python' and version == '3.8'))
print('\t{}'.format(language == 'Java' or language == 'Python'))
print('\t{}'.format(language == 'Pascal' or language == 'Javascript'))
print('\t{}'.format(not language == 'C'))

print('\n')