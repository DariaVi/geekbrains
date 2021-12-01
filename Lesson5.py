# one

one_file = open("text_1.txt", "w", encoding='utf-8')

line = " "
while line:
    line = input('Введите данные: ')
    one_file.write(f"{line}\n") if line != '' else one_file.close()

# two

with open("text_1.txt", encoding='utf-8') as f:
    two_line = f.readlines()
    for index, value in enumerate(two_line, 1):
        number = len(value.split())
        print(f'Количество слов {number} в строке {index}')

# three

with open("text_3.txt", "r", encoding='utf-8') as f:
    workers = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя величина дохода сотрудиников равна : {round(sum(workers.values()) / len(workers), 4)}\n'
          f'Список сотрудиков имеющие оклад ниже 20 тыс : {[a[0] for a in workers.items() if a[1] < 20000]}')

# four

number = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4_1.txt", "w", encoding='utf-8') as new_file:
    with open("text_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], number.get(line.split()[0])) for line in my_file])

# five

from random import randint

with open("text_5.txt", mode="w+", encoding='utf-8') as my_file:
    my_file.write(" ".join([str(randint(1, 50)) for a in range(25)]))
    my_file.seek(0)
    print(f'Сумма чисел равна - {sum(map(int, my_file.readline().split()))}')

# six
lesson_dict = {}
with open("text_6.txt", encoding='utf-8') as my_file:
    for line in my_file:
        name, number = line.split(':')
        name_sum = sum(map(int, "".join([i for i in number if i == '' or '9' >= i >= '0']).split()))
        lesson_dict[name] = name_sum
print(f'Общее количество часов по предмету - {lesson_dict}')

# seven
import json

with open("text_77.json", "w", encoding='utf-8') as true_file:
    with open("text_7.txt", encoding='utf-8') as f_file:
        result = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_file}
        res_one = [result, {"Medium_profit": round(sum([int(i) for i in result.values() if int(i) > 0]) / len(
            [int(i) for i in result.values() if int(i) > 0]))}]
    json.dump(res_one, true_file, ensure_ascii=False)
