"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division_func (n = int(input('Please enter a first number :')),m = int(input('Please enter a second number :'))):
    try:
        n/m
    except:
        ZeroDivisionError
        print('The division of numbers you entered is inadmissible because of the divisor is zero!')
    else:
        print(f'The division of numbers you entered is {round(n/m, 2)}')

division_func()


