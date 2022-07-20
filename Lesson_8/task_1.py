"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def transformation(cls, date):
        my_date = []
        for i in date.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day,month,year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2010 <= year <= 2030:
                    print("The date is correct!")
                else:
                    print("The year is incorrect!")
            else:
                print("The month is incorrect!")
        else:
            print("The day is incorrect!")

    def __str__(self):
        print(f"The current date is {Data.transformation(self.date)}")

today = Data('9-07-2022')
Data.validation(10,7,2022)
Data.validation(32,7,2032)
Data.validation(10,7,2032)
Data.validation(10,13,2015)

