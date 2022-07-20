"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class Error:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def devide_by_zero(dividend, divisor):
        try:
            dividend / divisor
            print("The division is admissible.")
        except:
            print("The division by zero is not admissible.")


Error.devide_by_zero(100,10)
Error.devide_by_zero(100,0)
