"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open ("task1.txt", 'w') as create_task1_file:
    while True:
        a = input("Please input some value or just press Enter to quit: ")
        if a != "":
            print(a, file = create_task1_file)
            continue
        else:
            break



