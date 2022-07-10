"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNumber:

    def __init__(self,re,im,*args):
        self.im = im
        self.re = re
        self.z = 're + im * j'

    def __add__(self, other):
        print(f"The addition of z1 and z2 equals {self.re + other.re} + {self.im + other.im}*j")

    def __mul__(self, other):
        print(f"The multiplication of z1 and z2 equals {self.re + other.re - (self.im * other.im)} + {self.re + other.re}*j")


z1 = ComplexNumber(10,-20)
z2 = ComplexNumber(-5,4)
z1 + z2
z1 * z2


