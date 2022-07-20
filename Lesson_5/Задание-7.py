"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

res = []
res_dict = {}
positive_profit_count = 0
total_profit = 0

with open('task7_input.txt', 'r') as my_file:
    for line in my_file:
        company, _, rev, exp = line[:-1].split()
        profit = int(rev) - int(exp)
        if profit > 0:
            total_profit += profit
            positive_profit_count += 1
        res_dict[company] = profit
avr_profit = total_profit / positive_profit_count if positive_profit_count else 0
res.append(res_dict)
res.append({'An average_profit': round(avr_profit,2)})

with open('task7_output.txt', 'w') as file:
    json.dump(res, file)