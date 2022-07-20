"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Kicking off drawing')

class Pen(Stationery):
    def draw(self):
        print(f'This is pen {self.title} to draw.')

class Pencil(Stationery):
    def draw(self):
        print(f'This is pencil {self.title} to draw.')

class Handle(Stationery):
    def draw(self):
        print(f'This is handle {self.title} to draw.')

pilot = Pen('Pilot')
pilot.draw()

erich_krause = Pencil('Erich Krause')
erich_krause.draw()

konus = Handle('Конус')
konus.draw()




