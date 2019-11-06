while(1):
    expression = input('Type an expression: ')

    tokens = expression.split(" ")

    x = float(tokens[0])
    operator = tokens[1]
    y = float(tokens[2])

    if operator == '+':
        print("{} {} {} = {}".format(x, operator, y, (x + y)))

    elif operator == '-':
        print("{} {} {} = {}".format(x, operator, y, (x - y)))
    
    elif operator == '*':
        print("{} {} {} = {}".format(x, operator, y, (x * y)))    
    
    elif operator == '/':
        print("{} {} {} = {}".format(x, operator, y, (x / y)))
    
    elif operator == '**':
        print("{} {} {} = {}".format(x, operator, y, (x ** y)))
    
    elif operator == ' //':
        print("{} {} {} = {}".format(x, operator, y, (x // y)))
    
    else:
        print('Invalid!')