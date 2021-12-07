# one

# import time
# import itertools


# class TrafficLight:
# __color = [["Красный", [7, 31]], ["Жёлтый", [2, 33]], ["Зелёный", [9, 32], ["Жёлтый", [2, 33]]]]

# def running(self):
# for colors in itertools.cycle(self.__color):
# print(f"\r\033[{colors[1][1]}m\033[1m{colors[0]}\033[0m", end="")
# time.sleep(colors[1][0])


# tl = TrafficLight()
# tl.running()


# two

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_asf(self, weight=25, tn=5):
        return f'Масса асфальта, необходимого для покрытия всего дорожного полотна: ' \
               f'{self._length} м * {self._width} м * {weight} кг * {tn} см = ' \
               f'{(self._length * self._width * weight * tn) / 1000} т'



road_one = Road(5000, 20)
print(road_one.weight_asf())


#three

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


workers = Position("Иванов", "Иван", "Прораб", 80000, 50000)
print(workers.get_full_name())
print(workers.position)
print(workers.get_total_income())

#four
from random import choice


class Car:
    """Прототип машины"""
    direction = ["север", "юг", "запад", "восток", "северо-запад", "северо-восток", "юго-запад", "юго-восток"]

    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.police = police
        print(f'Машина {name} имеет цвет {color}.\n Это полицейская машина? {police}')

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        print(f'Машина {self.name} повернула на {choice(self.direction)}')

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}.'


class TownCar(Car):
    """Городская машина"""

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}. ' \
               f'Превышение!!!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """Рабочая машина"""

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}. ' \
               f'Превышение!!!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """Спортивая машина"""

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}. ' \
               f'Превышение!!!' if self.speed > 120 else super().show_speed()


class PoliceCar(Car):
    """Полицейкая машина"""

    def __init__(self, name, color, speed, police=True):
        super().__init__(name, color, speed, police=True)

police_car = PoliceCar('"Lada Granta"', 'бело-синий', 80)
work_car = WorkCar('"Kia Rio"', 'серебристый', 39)
sport_car = SportCar('"Subaru"', 'красный', 121)
town_car = TownCar('"Audi A3"', 'черный', 70)

list_cars = [police_car, work_car, sport_car, town_car]

for i in list_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()


#five

class Stationery:
    def __init__(self, title="предмета для рисования"):
        self.title = title

    def draw(self):
        print(f'начнем рисование с помощью {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'начнем рисование с помощью ручки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'начнем рисование с помощью карандаша {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'начнем рисование с помощью фломастера {self.title}')


stationery_one = Stationery()
pen_one = Pen('Erich Krause')
pencil_one = Pencil('Koh-I-Noor Mondeluz')
handle_one = Handle('ShinhanArtTouch Brush')


art_supplies = [stationery_one, pen_one, pencil_one, handle_one]

for i in art_supplies:
    i.draw()



