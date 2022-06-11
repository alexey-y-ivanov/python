"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

file = sys.argv
hours = int(sys.argv[1])
rate_per_hour = int(sys.argv[2])
bonus = int(sys.argv[3])

def calculation (hours, rate_per_hour, bonus):
    return (hours * rate_per_hour) + bonus

result = calculation(hours, rate_per_hour, bonus)

print('Script', file)
print('Hours :', hours)
print('Rate per hour :', rate_per_hour)
print('Bonus :', bonus)
print('Total :', result)
