"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
"""

def my_func(x = int(input('Please enter a number which will be raised to the power of a number to be input at the next step :')),y = int(input('Please enter a negative number which absolute value will raise the power of the previous number:'))):
    print(f'Here are the numbers you entered: {x} and {y}. The first number raised to the power of the ablsolute value of the second results in {x ** abs(y)}')

my_func()
