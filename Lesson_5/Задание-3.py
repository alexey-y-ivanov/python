"""
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('task3.txt', 'r') as my_file:
    while True:
        content = my_file.readline()
        salary = [int(s) for s in content.split() if s.isdigit()] # parsing numbers from lines
        for x in salary:
            if x < 20000:
                print(f' {content}. The employee salary is below 20000.')

        if not content:
            break
