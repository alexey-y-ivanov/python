"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
season = {1:'Winter', 2: 'Winter', 3: 'Spring', 4:'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

a = int(input('Please input a number of a month: '))

print(f'The inserted number of a month belongs to the {season[a]} season')

