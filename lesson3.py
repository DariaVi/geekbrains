# one

def division(a1, a2):
    try:
        a1, a2 = int(a1), int(a2)
        c = a1 / a2
    except ZeroDivisionError:
        return 'На 0 делить нельзя!'
    except ValueError:
        return 'Это не число!'
    return c


print(division(input("Введите число a1 = "), input("Введите число a2 = ")))


# two

def data(name, surname, year, city, email, phone):
    return f'Имя - {name}, Фамалия - {surname}, Год рождения - {year}, Город - {city}, Почта - {email}, ' \
           f'Телефон - {phone}'


print(data(name='Мария', surname='Иванова', year='12.11.1989', city='СПб',
           email='mivanova@mail.ru', phone='8-985-454-31-74'))


# three
def my_func(a, b, c):
    return sum(sorted([a, b, c])[1:])

print(f'Сумма двух наибольших аргументов равна - {my_func(5454, 2444, 7452)}')


# four
def degree_func(x, y):
    try:
        x, y = float(x), int(y)
        res = x ** y
    except TypeError:
        return "Ведите действительное положительное число x и целое отрицательное число y."
    return res


print(degree_func(input('Введите дейтсивтельное положительное число x: '),
                  input('Введите целое отрицательное число y: ')))


def degree_func1(x1, y1):
    try:
        res = 1
        x1, y1 = float(x1), int(y1)
        if x1 <= 0 or y1 >= 0:
            return "Ошибка!"
        else:
            for i in range(abs(y1)):
                res /= x1
        return f"Результат возведения: {round(res,8)}"
    except ValueError:
        return "Вводите только числа!"


print(degree_func1(input('Введите дейтсивтельное положительное число x1: '),
                   input('Введите целое отрицательное число y1: ')))


# five
def summa():
    t = 0
    while True:
        number = input('Введите число, или символ "&" для выхода: ').split()
        for num in number:
            if num.lower() == "&":
                return t
            else:
                try:
                    t += int(num)
                except ValueError:
                    print('Для выхода, введите "&".')
            print(f"Сумма чисел = {t}")


print(summa())


# six-seven

def word_func():
    for word in input('Вводите слова через пробел на латинице: ').split():
        symbols = 0
        for symbol in word:
            if 97 <= ord(symbol) <= 122:
                symbols += 1
                if symbols != len(word):
                    break
                else:
                    print(f'Вводить только на английской раскладке!{word}')
        print(word.title())


print(word_func())
