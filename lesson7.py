# three

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['#' * rows for _ in range(self.nums // rows)]) + '\n' + '#' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print("Объединение двух клеток")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Участие двух клеткок")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "В-первой клетке ячеек меньше, чем во-второй. Ошибка."

    def __mul__(self, other):
        print("Создание общей клетки из двух")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Создание общей клетки из двух")
        return Cell(self.nums // other.nums)


cell_one = Cell(15)
cell_two = Cell(12)
print(f"Сумма двух клеток равна - {cell_one + cell_two}")
print(f"Разность двух клеток равна - {cell_one - cell_two}")
print(f"Произведение двух клеток равно - {cell_one * cell_two}")
print(f"Деление двух клеток равно - {cell_one // cell_two}")
print(cell_two.make_order(5))

# One

from itertools import zip_longest


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(a) for a in b]) for b in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*q, fillvalue=0))
                       for q in zip_longest(self.matrix, other.matrix, fillvalue=[])])


mto = [[31, 22], [3, 5, 32], [3, 5, 8, 3]]
mtt = [[37, 43], [2, 4, 6]]

matrix_one = Matrix(mto)
matrix_two = Matrix(mtt)

print(f'Исходная первая матрица: \n{matrix_one}\n')
print(f'Исходная вторая матрица: \n{matrix_two}')
print(f'Матрица после сложения: \n{matrix_one + matrix_two}')

# two

from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, pr):
        self.pr = pr

    @property
    @abstractmethod
    def cost(self):
        pass

    def __add__(self, other):
        Clothes.result += self.cost + other.cost
        return Cost(0)

    def __str__(self):
        rest = Clothes.result
        Clothes.result = 0
        return f'{rest}'


class Palt(Clothes):
    @property
    def cost(self):
        return round(self.pr / 6.5) + 0.5


class Cost(Clothes):
    @property
    def cost(self):
        return round((2 * self.pr + 0.3) / 100)


palt = Palt(46)
cost = Cost(181)
print(f'Суммарный расход ткани на пошив ксотюма и ткани равен {palt + cost + palt} метрам')
