""""
6. Реализовать функцию int_func(),
принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""
def int_func(a = input("Please input a string starting with a lowercase letter: ")):
    print(f"Here's the string you entered: {a}. The string with the first uppercase letter is the following: {a.capitalize()}")

int_func()

