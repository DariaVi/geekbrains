# one
a = 25
b = 32
print("Переменные a", a, "и b", b)
country = input('Enter Your country- ')
age = input('Enter Your age- ')
city = input('Enter Your city- ')
house = input('Enter Your number house- ')
print('Введеные значения country', country,
      'Age', age,
      'City', city,
      'House', house)

# two
time = int(input("Ввести время в секундах"))
hours = time // 3600
min = (time - hours * 3600) // 60
sec = time - (hours * 3600 + min * 60)
print(f"Время {hours:02}:{min:02}:{sec:02}")

# three
n = input("Введите число больше 0 - ")
while n < '0':
    print("Повторите еще раз ввод числа больше 0 -")
    n = input("Введите число больше 0 - ")
print(f'Сумма равна {n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n +n)}')


# four
y = int(input('Введите число-'))
maximum = 0
while y > 0:
    y1 = y % 10
    if y1 >= maximum:
        maximum = y1
    y //= 10
print("Максимальное число-", maximum)

# five
positive = float(input('Введите прибыль предприятия-'))
negative = float(input('Введите издержки предприятия-'))
if positive > negative:
    print(f'Финансовый результат фирмы - прибыль. Рентабельность {100 * positive / negative:.3f}%')
    emp = int(input('Количество сотрудников-'))
    print(f'Прибыльность на одного сотрудника - {positive / emp: .3f}')
elif positive == negative:
    print(f'Финансовый результат фирмы - 0.')
else:
    print(f'Финансовый результат фирмы - убытки. Рентабельность {- 100 * negative / positive:.3f}%')

# six

d = int(input('Результаты первого дня в км '))
k = int(input('Желаемый результат в км '))
resd = 1
while d < k:
    d = d + d * 0.1
    resd += 1
print(f'На {resd} день будет достигнут результат в {k} км')