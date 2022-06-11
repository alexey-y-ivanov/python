"""
7. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""
def int_func(a = input("Please input a string comprising of few words separated with space and starting with lowercase letters: ")):
    print(f"Here's the string you entered: {a}. The string with the first uppercase letters in each word is the following: {a.title()}")

int_func()
