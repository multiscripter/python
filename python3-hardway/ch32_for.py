# Ссылочный тип Список (класс List).
# https://docs.python.org/3.6/tutorial/datastructures.html
# pydoc list

girltypes = ['блондинка', 'брюнетка', 'шатенка', 'рыжая']
stuff = [1, 'второй', 3.0, True]
empty = []
multi = [[1, 2, 3], [4, 5, 6]]

# Цикл for. Вариант 1.
for gtype in girltypes:
	print(f"Тёлочка: {gtype}")

for a in stuff:
	print(f'Добавляю {a} в список empty')
	empty.append(a)

for b in range(0, 6):
	print('b:', b)

print(girltypes[2]) # Выведет: шатенка
print(multi[1][1]) # Выведет: 5

# Почти классический/
for c in range(0, len(girltypes)):
	print(girltypes[c])

# Methods: 

# list.append(x)
# list.extend(iterable)
# list.insert(i, x)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[, start[, end]])
# list.count(x)
# list.sort(key=None, reverse=False)
# list.reverse()
# list.copy()