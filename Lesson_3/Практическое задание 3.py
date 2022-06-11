"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""

def my_func(a = int(input('Please enter a first number :')), b = int(input('Please enter a second number :')), c = int(input('Please enter a third number :'))):
    list = [a,b,c]
    list = sorted(list, reverse=True)
    print(f'The maximum numbers you inserted are {list[0]} and {list[1]}. Their sum is {list[0] + list[1]}.')

my_func()