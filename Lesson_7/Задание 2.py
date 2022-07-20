"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

import abc

class Clothes(abc.ABC):
    abc.abstractmethod # turns Clothes into an abstract class which isn't supposed to create objects
    def textile_calculation(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = V
    @property # the given below method "textile_calculation" will be regarded as an attribute returning the V value
    def textile_calculation(self):
        V = round(self.V/6.5 + 0.5, 2)
        return V

class Suit(Clothes):
    def __init__(self, H):
        self.H = H
    @property # the given below method "textile_calculation" will be regarded as an attribute returning the H value
    def textile_calculation(self):
        H = round(2*self.H + 0.3, 2)
        return H

c1 = Coat(10)
s1 = Suit(20)
print(f"It's required {c1.textile_calculation} textile for the coat.")
print(f"It's required {s1.textile_calculation} textile for the suit.")
print('The total textile utilization:', round(c1.textile_calculation + s1.textile_calculation, 2))


