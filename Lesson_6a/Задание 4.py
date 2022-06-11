"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, plate, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Car:
    speed: int
    colot: str
    plate: str
    is_police: bool

    def __init__(self, speed, color, plate, is_police):
        self.speed = speed
        self.color = color
        self.name = plate
        self.is_police = is_police
    def show_speed(self):
        print(f' The current speed is {self.speed} km/h')
    def go(self):
        print('The car started moving')
    def stop(self):
        print('The car stopped')
    def turn_left(self):
        print('The car turned left')

class TownCar(Car):
    def show_speed(self):
        print(f' The current speed is {self.speed} km/h')
        if self.speed > 60:
            print('The speed threshold is exceeded!')

class WorkCar(Car):
    def show_speed(self):
        print(f' The current speed is {self.speed} km/h')
        if self.speed > 40:
            print('The speed threshold is exceeded!')

class SportCar(Car):
    def sport_car(self):
        print('This is a sport car')

class PoliceCar(Car):
    def police_car(self):
        if self.is_police is True:
            print('This is a police car')

opel = TownCar(50, 'biege', 'E184BH777', False)
gazel = WorkCar(60, 'blue', 'A001KM777', False)
ford = SportCar(160, 'red', 'M784HH197', False)
lada = PoliceCar(160, 'red', 'P562OP777', True)

opel.show_speed()
opel.go()
gazel.show_speed()
ford.sport_car()
ford.show_speed()
lada.turn_left()
lada.police_car()






