"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
with open ('task5.txt', 'w') as my_file_write:
    print('10 20 30 40 50', file = my_file_write)

with open ('task5.txt', 'r') as my_obj:
    content = my_obj.readline()
    my_list = content.split()
    result = [int(j) for j in my_list]
    print(f'The sum of your list equals {sum(result)}')
