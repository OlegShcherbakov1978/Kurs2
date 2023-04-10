# Задача 1. Продукты
# Необходимо написать функцию, принимающую неопределенное количество аргументов.
# Принимаемые аргументы могут содержать множество различных данных,
# но требуются найти среди них лишь список продуктов, которые записаны просто
# в виде строк. Если продуктов не нашлось, то вывести соответствующее сообщение.

# Примеры вызова и вывода функции

# Вызов #1:

# printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)

# Вывод #1:

# 1) Бананы
# 2) Яблоки
# 3) Макароны
# 4) Кофе

groceries = ('Бананы', 'Яблоки', 'Макароны', 'Кофе')


def func(*args):

    my_list = list(filter(lambda x: type(x) == str and x in groceries, args))
    return my_list


a = (func('Бананы', [1, 2], ('Python'), 'Яблоки',
          '', 'Макароны', 5, True, 'Кофе', False))


if len(a) > 0:
    for i in range(1, len(a)+1):
        print(f'{i}) {a[i-1]}')

else:
    print("продукты отсутствуют")
