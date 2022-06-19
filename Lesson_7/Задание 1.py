"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:

    def __init__(self, listing):
        self.listing = listing

    def __str__(self):
        s = ''
        for i in range(len(self.listing)):
            s = s + '\t'.join(map(str, self.listing[i])) + '\n' # \t stands for tab
        return s

    def __add__(self, other):
        for i in range(len(self.listing)):
            for j in range(len(self.listing[i])):
                self.listing[i][j] = self.listing[i][j] + other.listing[i][j]
        return Matrix.__str__(self)

m1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
print(f"Here's matrix m1: \n{m1}")
m2 = Matrix([[10,11,12], [13,14,15], [16,17,18]])
print(f"Here's matrix m2: \n{m2}")
m3 = m1.__add__(m2)
print(f"The resulting matrix is the following: \n{m3}")









