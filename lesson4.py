# one
# from sys import argv
# name, hours, stav, prem = argv
# calculation = (int(hours) * int(stav)) + int(prem)
# print(f'Заработная плата сотрудника {calculation}')


# two

my_list_one = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_two = [a for n, a in enumerate(my_list_one) if my_list_one[n - 1] < my_list_one[n]]
print(f'Список чисел {my_list_one}')
print(f'Список чисел после преобразования {my_list_two}')

# three

print(
    f'Список чисел от 20 до 240, которые кратны 20 или 21, равен: {[i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]}')

# four
one_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
two_list = [i for i in one_list if one_list.count(i) == 1]
print(f'Список чисел не имеющих повторений: {two_list}')

# five

from functools import reduce

chet_number = [i for i in range(100, 1001) if i % 2 == 0]
multi = reduce((lambda x, y: x * y), chet_number)
print(f'Результат вычисления произведения равен : {multi}')

# six

from itertools import count, cycle

count_spring = count(9)
cycle_mon = cycle("SON")

for _ in range(3):
    print('(count_spring, cycle_mon = ({}, {})'.format(next(count_spring), next(cycle_mon)))

# seven
from itertools import count

from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)


x = 0
for i in fact_gen():
    if x == 15:
        break
    else:
        x += 1
        print(f'Факториал {x} = {i}')
