"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""

class MyError(Exception): # Exception stands for the basic class of all available exceptions
    def __init__(self):
        pass

class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global my_value
        while True:
            try:
                try:
                    my_value = int(input("Please input a number: "))
                    self.my_list.append(my_value)
                    b = input("Please input another number or type 'stop' to quit: ")
                    if b == 'stop':
                        print(f"Here's the list {self.my_list} of your numbers")
                        break
                except ValueError:
                    raise ValueError
            except MyError:
                b = input(f"The type isn't a number. Please input another number or type 'stop' to quit: ")
                if b == 'stop':
                    print(f"Here's the list {self.my_list} of your numbers")
                    break
                else:
                    self.check_value()

d = TypeCheck()
d.check_value()




