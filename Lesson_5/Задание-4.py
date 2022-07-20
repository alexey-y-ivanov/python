"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open ('task4(english).txt', 'r') as english_file:
    while True:
        content = english_file.readline()
        list_line = content.split()
        # matching list_line elements with my_dict
        for i in list_line:
            if i in my_dict:
                with open("task4(russian).txt", 'a') as russian_file:
                    print(f'{my_dict[i]} {list_line[1]} {list_line[2]}', file=russian_file)
        if not content:
            break

