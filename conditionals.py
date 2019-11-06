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
print(x > y)
print(x == y)
print(x < y)

print('\Result: ')
if x > y:
    print('X > Y')
elif x == y:
    print('X == Y')
else:
    print('X < Y')

print('\n')

language = input('Language: ').capitalize()
version = input('Version: ')

if language == 'Python' and version == '3.8':
    print('Version 3.8')

if language == 'Java' or language == 'Python':
    print('Python or Java')
elif language == 'Pascal' or language == 'Javascript':
    print('Pascal or Javascript')

if not language == 'C':
    print('Not C')

print('\n')
print(language == 'Python' and version == '3.8')
print(language == 'Java' or language == 'Python')
print(language == 'Pascal' or language == 'Javascript')
print(not language == 'C')
