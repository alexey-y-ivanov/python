"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

list = [1, True, [1,2], 'string', ('a','b'), {'key': 'value'}, None]

for i in list:
    print(type(i))