# two
class ZeroError(Exception):
    def __init__(self, num):
        self.num = num


def floordiv(s_1, s_2):
    print("Деление")
    try:
        if s_2 == 0:
            raise ZeroError('На 0 делить нельзя! Введите еще раз числа для деления')
    except ZeroError as error:
        return error
    else:
        return ZeroError(s_1 // s_2)


zero_one = int(input('Введите числа для деления: '))
zero_two = int(input('Введите числа для деления: '))

print(f'Результат деления числа равен {floordiv(zero_one, zero_two)}')


# three

class ValEr(Exception):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список, если хотите закончить список, введите @: ')
        if value == '@':
            break
        if not value.isdigit():
            raise ValEr(value)
        my_list.append(int(value))
    except ValEr as ex:
        print('Ошибка! Вводить можно только числа! Для выхода нажмите @', ex)
print(f'Итоговый список равен {my_list}')


# one

class Date(object):

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def none(cls, day_month_year):
        nn_dt = []

        for i in day_month_year.split():
            if i != '-': nn_dt.append(i)

        return int(nn_dt[0]), int(nn_dt[1]), int(nn_dt[2])

    @staticmethod
    def normal(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Успех.'
                else:
                    return f'Ошибка! Введите верный год.'
            else:
                return f'Ошибка! Введите верный месяц.'
        else:
            return f'Ошибка! Введите верный день.'

    def __str__(self):
        return f'Текущая дата {Date.none(self.day_month_year)}'


today = Date('08 - 12 - 2021')
print(f'Сегодня {today}')
print(Date.normal(32, 12, 2022))
print(today.normal(11, 13, 2017))
print(Date.none('01 - 01 - 2022'))
print(today.none('31 - 12 - 2021'))
print(Date.normal(15, 12, 2002))


# seven

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Производим сложение...')
        return f'q = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Производим умножение...')
        return f'q = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'q = {self.a} + {self.b} * i'


q_1 = ComplexNumber(-21, 5)
q_2 = ComplexNumber(30, 11)
print(f'Первое комплексное число: {q_1}')
print(f'Второе комплексное число: {q_2}')
print(f'Сумма комплексных чисел: {q_1 + q_2}')
print(f'Произведение комплексных чисел: {q_1 * q_2}')

#four-six


class Warehouse:
    def __init__(self, name, price, quantum, *args):
        self.name = name
        self.price = price
        self.quantum = quantum
        self.wh_full = []
        self.wh_empty = []
        self.info_product = {'Наименование товара': self.name, 'Цена за единицу товара': self.price,
                             'Количество товара': self.quantum}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantum}'

    def rec(self):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.info_product.update(unique)
            self.wh_empty.append(self.wh_empty)
            print(f'Текущий список -\n {self.wh_empty}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода введите - N/n , для продолжения - Enter')
        q = input()
        if q == 'N' or q == 'n':
            self.wh_full.append(self.wh_empty)
            print(f'Весь склад -\n {self.wh_full}')
            return f'Выход'
        else:
            return Warehouse.rec(self)


class Print(Warehouse):
    def to_print(self):
        return f'Принтер {self.wh_empty}'


class Scan(Warehouse):
    def to_scan(self):
        return f'Сканер {self.wh_empty}'


class Xerox(Warehouse):
    def to_copier(self):
        return f'Ксерокс {self.wh_empty}'


unit_1 = Print('Print', 40000, 53)
unit_2 = Scan('Scanner', 80000, 89)
unit_3 = Xerox('Xerox', 35000, 27)
print(f'{unit_1.rec()}, {unit_2.rec()}, {unit_3.rec()}')