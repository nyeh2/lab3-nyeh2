#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: nyeh2

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        ans = int(number1) + int(number2)

    elif operator == 'subtract':
        ans = int(number1) - int(number2)

    elif operator == 'multiply':
        ans = int(number1) * int(number2)

    else:
        ans = ('Error: function operator can be "add", "subtract", or "multiply"')
    
    return(ans)

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))