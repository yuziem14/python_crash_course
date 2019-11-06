from math import sqrt # Module sqrt from math package

# Declaring Functions
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def up(num1, num2):
    return num1 ** num2

def div_floor(num1, num2):
    return num1 // num2

option = '0'

while(option != '3'):
    
    print('\t\t----------- MENU -----------')
    print('\t\t[1]. Calculate expression')
    print('\t\t[2]. Calculate square root')
    print('\t\t[3]. Exit')
    print('\t\t----------------------------')
    option = input('\t\t> ')

    if option == '1':
        expression = input('\t\tType an expression: ')
        tokens = expression.split(" ")
        x = float(tokens[0])
        operator = tokens[1]
        y = float(tokens[2])

        if operator == '+':
            print("\t\t{} {} {} = {}".format(x, operator, y, add(x, y)))
        elif operator == '-':
            print("\t\t{} {} {} = {}".format(x, operator, y, sub(x, y)))
        elif operator == '*':
            print("\t\t{} {} {} = {}".format(x, operator, y, mult(x, y)))    
        elif operator == '/':
            print("\t\t{} {} {} = {}".format(x, operator, y, div(x, y)))
        elif operator == '**':
            print("\t\t{} {} {} = {}".format(x, operator, y, up(x, y)))
        elif operator == '//':
            print("\t\t{} {} {} = {}".format(x, operator, y, div_floor(x, y)))
        else:
            print('\t\tInvalid Operation!')

    elif option == '2':
        x = float(input('\t\tType the value: '))
        print('\t\tThe Square Root of {} is {}'.format(x, sqrt(x)))
    
    elif option == '3':
        print('\t\tSee ya!')

    else:
        print('\t\tInvalid Option!')

    print('\n')