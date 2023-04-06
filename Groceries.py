groceries1 = ('Бананы', [1, 2], ('Python'), 'Яблоки',
              '', 'Макароны', 5, True, 'Кофе', False)
groceries2 = ('Бананы', 'Яблоки', 'Макароны', 'Кофе', 'Специи', 'Хлеб')
print((groceries1))


groceries1 = list(filter(lambda x: x in groceries2, groceries1))

print(*groceries1)
