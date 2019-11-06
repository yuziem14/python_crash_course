# Names
'''
@var  | No.
$Var  | No.
1Var  | No.
_var  | Ok.
var   | Ok.
VAR   | Ok.
var_1 | Ok.
var1  | Ok.
'''

# Declaring Variables
'''
x = 10         # int
y = 5.0        # float
name = 'Yuri'  # str
isMale = True  # bool
'''

# Multiple Assignment
x, y, name, isMale, age = (10, 5.0, 'Python', True, None)

# Retrieving types
print(type(x))
print(type(y))
print(type(name))
print(type(isMale))

# Casting
x = float(x)

# Printing
print('Hello, World!')

# Format Strings (2.x)
print('Type X = {}'.format(type(x)))
print('Type X = {type}'.format(type=type(x)))
print('Hello {name}. {isMale}. (x, y) = ({x}, {y}). Age: {age}\n'.format(
    name=name, isMale=isMale, x=x, y=y, age=age))

# Input
x = float(input('X Input: '))
print('X = {}\n'.format(x))

# Math Operations
'''
total = x + y
total = x - y
total = x * y
total = x / y
total = x // y
total = x ** y
'''

total = (x + y) / 3
print('Total = ' + str(total))
