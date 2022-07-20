"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

with open ("task2.txt", "r") as my_file:
    n = 1
    while True:
        content = my_file.readline()
        word_count = len(content.split())
        print(f' The {n} line is "{content}". It comprises of {word_count} words.')
        n = n+1
        if not content:
            break

