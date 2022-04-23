"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.

6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""

revenue = int(input('Please input a current value of your total revenue in RUR :'))
expenses = int(input('Please input a current value of your total expenses in RUR :'))


if revenue > expenses:
    print('Your business if profitable at the moment. Keep running it this way! The current profit ratio is :', ((revenue - expenses)/revenue))
    employees = int(input('Please input a current number of your employees :'))
    print('The revenue per employee results in :', revenue/employees, ' RUR')

else:
    print('Your busines is sustaining losses at the moment. You should revise it!')


