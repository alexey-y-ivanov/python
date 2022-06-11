"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
"""
a = input('Please input a string containing words separated with space :')
b = a.split()
print(b)

for count,values in enumerate(b,start=1):
    print(count,values[:10])

