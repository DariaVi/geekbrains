# one
my_list = [14, 17.12, 'October', True, [2021, 11.12], {'season': 'Autumn', 'weather': 'Cloudy'}]
for i in my_list:
    print(f'Проверка типа {i} относится к {type(i)}')

# two
lis = list(input('Введите значения для обмена: '))
for i in range(1, len(lis), 2):
    lis[i - 1], lis[i] = lis[i], lis[i - 1]
print(f'Значения после обмена : {lis}')

# three

month = int(input('Введите номер месяца - '))
seasons = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
res = 'Такого номера месяца нет. Введите еще раз'
for name, mon in seasons.items():
    if month in mon:
        res = name
        break
print(f'Данный номер месяца относится к времени года - {res}')

mon_s = int(input('Введите номер месяца - '))
mon_list = ['Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь']
for i in mon_list:
    print(f'Введеный номер месяца относится к - {mon_list[mon_s - 1]}')

# four
words = input('Введите слова: ').split(' ')
for i, word in enumerate(words, 1):
    print(f'Введеные слова: {i}) {word}'
          if len(word) <= 10
          else f'{i}) {word[:10]}')

# five
my_list = [7, 5, 3, 3, 2]
new = int(input('Новый элемент рейтинга: '))
i = 0
for y in my_list:
    if new <= y:
        i += 1
    else:
        break
my_list.insert(i, new)
print(f'Новый рейтинг: ', my_list)
