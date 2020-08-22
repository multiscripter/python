# Словари (HashMap. Элемнеты и ключи могут быть разных типов!)
# https://docs.python.org/3.6/library/stdtypes.html#dict

dikt = {
	'name': 'John',
	'age': 39,
	'height': 1.93,
	0.1: 'decimal key',
	1: 'int key',
	True: 'boolean is integer value in Python (1 - True, 0 - False)',
	None: '"None" type key'
}

print(dikt['name'])
dikt['location'] = 'Moscow'
print(dikt['location'])
print('dikt[1]:', dikt[1]) # boolean is integer value in Python (1 - True, 0 - False)
print('dikt[True]: ', dikt[True]) # boolean is integer value in Python (1 - True, 0 - False)
print(dikt[0.1]) # decimal
print(dikt[None])

del dikt[True] # Удалить элемент по ключу.
#print('dikt[1]:', dikt[1]) # Ошибка: KeyError: 1

print('=' * 50)

print(dikt) # Строковое представление словаря.

print('=' * 50)

# Обход значений словаря.
for key, val in list(dikt.items()):
	print(f'key: {key}, val: {val}')

print('=' * 50)

k = 'ololo'
unknown = dikt.get(k)
if not unknown:
	print(f'Нет значения по ключу {k}')