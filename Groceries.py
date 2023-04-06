groceries1 = ('Бананы', [1, 2], ('Python'), 'Яблоки',
              '', 'Макароны', 5, True, 'Кофе', False)
groceries = ('Бананы', 'Яблоки', 'Макароны', 'Кофе', 'Специи', 'Хлеб')


def func(my_list):

    my_list = list(filter(lambda x: x in groceries, my_list))
    return my_list


a = func(groceries1)
print(*a) if len(a) > 0 else print("данные для вывода отсутствуют")
