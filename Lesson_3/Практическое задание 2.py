"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""
def person(**kwargs):
    return kwargs

print(person(name = input('Please enter your name: '), surname = input('Please type your surname :'), city = input('Please enter the city you live in :'), year_of_birth = int(input('Please input your year of birth :')), email = input('Please enter your e-mail :'), phone = input('Please enter your phone :')))

