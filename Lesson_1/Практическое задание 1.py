"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
"""

n = int(input('Please input some number :'))
print(n)
print(type(n))

m = input('Please input some string :')
print(m)
print(type(m))

a = [1,2,3]
print(type(a))

b = ('Anna', 'Bill', 'Kate')
print(type(b))

c = False
print(type(c))

d = 1 + 1j
print(type(d))

cities = {'Moscow', 'Vienna', 'Rome'}
print(type(cities))

person = {
    'name':'Elisabeth',
    'surname': 'Andersson',
    'age': 27,
    'job_title': 'HR Manager',
    'location': 'Brussels'
}
print(type(person))
